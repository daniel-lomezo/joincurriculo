from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import ListaCasamento
# Register your models here.

class ListaCasamentoAdmin(ModelAdmin):
    icon_name = "person_outline"

    list_display = ("nome_item", "medida_item", "preferencia_cor", "tipo_lista", "item_ja_escolhido")
    list_filter = ("tipo_lista", "item_ja_escolhido")
    search_fields = ("nome_item", "medida_item", "preferencia_cor", "tipo_lista", "item_ja_escolhido")

    fieldsets = (("Listagem dos Itens", {"fields": ("pk", "nome_item", "medida_item", "preferencia_cor", "tipo_lista", "item_ja_escolhido")}),)

admin.site.register(ListaCasamento, ListaCasamentoAdmin)