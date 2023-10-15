from django import forms

class FormTelegram(forms.Form):
	nome = forms.CharField(label='Seu nome', max_length=100)
	email = forms.EmailField()
	id_telegram = forms.CharField(label='Seu ID Telegrm ou Número', max_length=80)
	messagem = forms.CharField(widget=forms.Textarea)

