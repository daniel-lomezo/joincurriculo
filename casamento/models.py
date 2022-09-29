from django.db import models

# Create your models here.
class TipoLista:
    LISTA_CASAMENTO = "lista de casamento"
    LISTA_PANELA = "Lista chá de panela"
    CHOICES = (
        (LISTA_PANELA, ("chá de panela")),
        (LISTA_CASAMENTO, ("presente de casamento")),
    )

class ListaCasamento(models.Model):
    nome_item = models.CharField(max_length=300, null=True, blank=True, verbose_name="Nome do Item")
    medida_item = models.CharField(max_length=300, null=True, blank=True, verbose_name="Medida do Item")
    preferencia_cor = models.CharField(max_length=300, null=True, blank=True, verbose_name="Preferência de cor")
    tipo_lista = models.CharField(max_length=300, null=True, blank=True, verbose_name="Tipo da Lista", choices=TipoLista.CHOICES)