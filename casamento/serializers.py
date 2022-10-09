import ast
import json
import logging
import uuid
from typing import Optional

from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from casamento.models import ListaCasamento

LOGGER = logging.getLogger(__name__)

class ListaCasamentoSerializer(serializers.ModelSerializer):


    class Meta:
        model = ListaCasamento
        fields = [
            "nome_item",
            "medida_item",
            "preferencia_cor",
            "tipo_lista",
            "item_ja_escolhido",
            "codigo_seguranca",
        ]