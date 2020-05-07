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





# Create your views here.

def curriculo_inicio(request):
	
	fornacaolist = {}
	fornacaolist['fornacaolist'] = formacao.objects.order_by('nomecurso').all()
	
	return render(request, 'curriculo.html',  fornacaolist)



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

		return redirect('/curriculo/')

	return redirect('/curriculo/')

		
	
def redirecionamento(request):
	return redirect('/curriculo/')










