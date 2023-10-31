import requests
from django.db import models

# Create your models here.
from ragcp.settings import logger
from users.models import Login


class Post(models.Model):
    title = models.CharField(max_length=256, help_text='O título da postagem')
    author = models.ForeignKey(Login, on_delete=models.CASCADE,
                               verbose_name='Criado por',
                               help_text='Conta que criou esta entrada. Caso venha de outra rede social, usará qualquer conta do sistema')
    content = models.TextField(null=True, blank=True,
                               help_text='o corpo da postagem')
    reference = models.CharField(max_length=2048, null=True, default=None,
                                 help_text='Link para a postagem original caso venha de outra rede social')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               default=None, verbose_name='Em resposta a',
                               help_text='Chave estrangeira para outro post caso seja uma resposta')
    deleted = models.BooleanField(default=False, null=True)

    added = models.DateTimeField(auto_now_add=True,
                                 help_text='Data em que foi criado no RagCP')
    updated = models.DateTimeField(auto_now=True,
                                   help_text='Data em que foi modificado')
    scoring = models.FloatField(max_length=28, null=True, default=None)
    scoring_label = models.CharField(max_length=64, default=None, null=True)

    def __str__(self):
        return '%s: %s by %s' % (
        self.title[:10], self.content[:40], self.author.username)

    def analyze_content(self):
        uri = 'https://natural-language-understanding-demo.ng.bluemix.net/api/analyze'
        headers = {
            'Content-Type': 'application/json'
        }
        data = '{"features": {"sentiment": {},"emotion":{}},"text": "%s"}' % self.content
        results = requests.post(uri, data=data, headers=headers)
        if results.status_code == 200:
            results = results.json()
            sentiment = results['results']['sentiment']['document']
            emotions = results['results']['emotion']['document']['emotion']
            label = ''
            first = False
            for emotion in emotions:
                if emotions[emotion] <= 0.5:
                    continue
                elif first:
                    label += ', %s' % emotion
                else:
                    label += '%s' % emotion
                    first = True
            sentiment['label'] = label or 'neutral'
            return sentiment
        else:
            results = results.json()
            logger.warning('Ocorreu um problema ao analisar a postagem %s, %s' % (self.id, results))
            if results['error'] == 'texto insuficiente para o ID do idioma':
                return {'score': 0, 'label': 'cannot analyze'}
            return {'score': 0, 'label': 'neutral', 'error': True}

    @property
    def sentiment_score(self):
        if self.parent is None:
            return 1
        elif not self.scoring:
            return self.analyze_content()['score']
        else:
            return self.scoring

    @property
    def sentiment_label(self):
        if self.parent is None:
            return 'not analyzed'
        elif not self.scoring_label:
            return self.analyze_content()['label']
        else:
            return self.scoring_label

    @property
    def sentiment(self):
        return self.analyze_content()

    def save(self, **kwargs):
        if self.parent is not None:
            analysis = self.analyze_content()
            scoring = analysis['score']
            label = analysis['label']

            if 'error' in analysis:
                super(Post, self).save()

            if scoring < 0:
                self.deleted = True
            self.scoring = scoring
            self.scoring_label = label
        super(Post, self).save()

    @property
    def num_responses(self):
        return Post.objects.filter(parent=self.pk, deleted=False).count()
