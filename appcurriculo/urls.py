from django.urls import path, include
from appcurriculo import urls as urls_curriculos
from appcurriculo.views import curriculo_inicio
from appcurriculo.views import viewexperiencia
from appcurriculo.views import submitemail
from appcurriculo.views import submit_telegram



urlpatterns = [
	path('dadospessoais/', curriculo_inicio, name='curriculo_inicio'),
	path('experiencias/', viewexperiencia, name='view_experiencia'),
	path('enviatelegram/submit/', submit_telegram, name='envia_telegram'),
	path('enviaemail/submit/', submitemail, name='envia_email'),


	]