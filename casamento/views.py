from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from rest_framework import status, mixins
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from django.shortcuts import render
from casamento.models import ListaCasamento
from casamento.serializers import ListaCasamentoSerializer
from telegram.telegrasms import Telegram


# Create your views here.
@csrf_exempt
@api_view(("POST",))
@permission_classes((AllowAny,))
def choice_item(request):
    id_tem = request.data.get("id_item")
    apelido = request.data.get("apelido")

    print(f"JSON = {apelido}")
    list_casamento = ListaCasamento.objects.get(pk=int(id_tem))

    list_casamento.item_ja_escolhido = False
    list_casamento.quem_escolheu = apelido
    list_casamento.save()

    list_casamento = ListaCasamento.objects.filter(pk=int(id_tem))

    print("------------------------------->", list_casamento.first().quem_escolheu)

    return Response(status=status.HTTP_200_OK)


@csrf_exempt
@api_view(("POST",))
@permission_classes((AllowAny,))
def list_casamento(request):
    tipo_lista = request.data.get("tipo_lista")
    print(f"JSON = {tipo_lista}")
    list_casamento = ListaCasamento.objects.filter(
                                                    tipo_lista="Lista chá de panela",
                                                    item_ja_escolhido=True
                                                    ).order_by("nome_item")
    print(list_casamento)
    serializer = ListaCasamentoSerializer(list_casamento, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

# Create your views here.
@csrf_exempt
@api_view(("POST",))
@permission_classes((AllowAny,))
def send_message_telegram(request):
    """
        {
            "nome_completo": "Daniel Lomezo",
            "phone_number": "21974164650",
            "message": "Oi tudo bem, como faço para obter código de confirmação"

            }

    """

    nome_completo = request.data.get("nome_completo")
    phone_number = request.data.get("phone_number")
    message = request.data.get("message")

    Telegram.bot_sendtextinfo('0', nome=nome_completo, email_phone_number=phone_number, mensagem=message, tipo_message="casamento")

    return Response(data="sucess", status=status.HTTP_200_OK)