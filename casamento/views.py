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


# Create your views here.
@csrf_exempt
@api_view(("POST",))
@permission_classes((AllowAny,))
def list_casamento(request):
    # {"tipo_lista": "Lista chá de panela"}
    # {"tipo_lista": "lista de casamento"}
    tipo_lista = request.data.get("tipo_lista")
    print(f"JSON = {tipo_lista}")
    list_casamento = ListaCasamento.objects.filter(tipo_lista=tipo_lista).order_by("nome_itema")
    print(list_casamento)
    serializer = ListaCasamentoSerializer(list_casamento, many=True)
    print(f'Serializer {serializer}')

    return Response(data=serializer.data, status=status.HTTP_200_OK)
        