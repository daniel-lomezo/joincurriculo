from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from .models import formacao
from .models import experiencia
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date





# Create your views here.

def curriculo_inicio(request):
	
	fornacaolist = {}
	fornacaolist['fornacaolist'] = formacao.objects.all()
	
	return render(request, 'curriculo.html',  fornacaolist)



def viewexperiencia(request):
	
	experiencialist = {}
	experiencialist['experiencialist'] = experiencia.objects.all()
	
	return render(request, 'experiencias.html',  experiencialist)





		
	
def redirecionamento(request):
	return redirect('/curriculo/')










