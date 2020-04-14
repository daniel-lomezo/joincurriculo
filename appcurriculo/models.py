from django.db import models

# Create your models here.

class formacao(models.Model):
	nomecurso = models.CharField(max_length=100)
	textdescricao = models.TextField()
	

	def __str__(self):
		return self.nomecusro


class experiencia(models.Model):
	nomeempresa = models.CharField(max_length=100)
	cargo = models.CharField(max_length=80)
	objetos = models.TextField()
	
	

	def __str__(self):
		return self.nomeempresa