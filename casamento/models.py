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
    item_ja_escolhido = models.BooleanField(null=True, blank=True, default=False, verbose_name="Item disponivel ou não", help_text="Se não estiver marcado o Item ainda não foi escolhido")
    codigo_seguranca = models.CharField(max_length=300, null=True, blank=True, verbose_name="Codigo de segurança", help_text="Para gerar um codigo clique aqui https://www.lastpass.com/pt/features/password-generator")
    quem_escolheu = models.CharField(max_length=400, null=True, blank=True, verbose_name="Quem escolheu", help_text="Nome de quem escolheu o item")

    def __str__(self):
        return f"{self.nome_item} ---- {self.tipo_lista}"