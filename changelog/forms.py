from django import forms

class BuyCoinsForm(forms.Form):
    account_id = forms.IntegerField(label='ID da Conta')
    key = forms.CharField(label='Chave')
    value = forms.IntegerField(label='Valor')