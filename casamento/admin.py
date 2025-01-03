from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import ListaCasamento
# Register your models here.

class ListaCasamentoAdmin(ModelAdmin):
    icon_name = "person_outline"

    list_display = ("id", "nome_item", "medida_item", "preferencia_cor", "tipo_lista", "item_ja_escolhido", "quem_escolheu")
    list_filter = ("tipo_lista", "item_ja_escolhido")
    search_fields = ("nome_item", "medida_item", "preferencia_cor", "tipo_lista", "item_ja_escolhido")

    fieldsets = (("Listagem dos Itens", {"fields": ("nome_item", "medida_item", "preferencia_cor", "tipo_lista", "item_ja_escolhido", "quem_escolheu")}),)

admin.site.register(ListaCasamento, ListaCasamentoAdmin)