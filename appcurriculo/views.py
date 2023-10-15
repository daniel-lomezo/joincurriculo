from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from .models import formacao
from .models import experiencia
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date
from emailpak.email import mail
from telegram.telegrasms import Telegram

# import formularios
from .forms import FormTelegram



# Create your views here.

def curriculo_inicio(request):
	
	fornacaolist = {}
	fornacaolist['fornacaolist'] = formacao.objects.order_by('nomecurso').all()
	

	return render(request, 'curriculo.html', fornacaolist)



def viewexperiencia(request):
	
	experiencialist = {}
	experiencialist['experiencialist'] = experiencia.objects.all()
	
	return render(request, 'experiencias.html',  experiencialist)




@csrf_protect
def submitemail(request):

	if request.POST:

	

		titulomensagem = request.POST.get('titulo')
		emailenvio = request.POST.get('email')
		mensagem = request.POST.get('mensagem')
		
		print(titulomensagem, emailenvio, mensagem)

		envia = mail.enviaemail('0', titulomensagem, mensagem, emailenvio)

		return redirect('curriculo_inicio')

	return redirect('curriculo_inicio')

def submit_telegram(request):

	if request.POST:

		nome = request.POST.get('nome')
		titulo = request.POST.get('titulo')
		email = request.POST.get('email')
		id_user = request.POST.get('idtelegram')
		mensagem = request.POST.get('mensagem')

		Telegram.bot_sendtextinfo('0', nome, titulo, email, id_user, mensagem)

		return redirect('curriculo_inicio')
		
	else:

		return redirect('curriculo_inicio')

	return redirect('curriculo_inicio')

	

def redirecionamento(request):
	return redirect('curriculo_inicio')







