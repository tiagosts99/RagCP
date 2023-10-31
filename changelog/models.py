from django.db import models

# Create your models here.
from django.db import models

class AccRegNum(models.Model):
    account_id = models.IntegerField()
    key = models.CharField(max_length=32)
    value = models.IntegerField()

    def __str__(self):
        return f"Account ID: {self.account_id}, Key: {self.key}, Value: {self.value}"