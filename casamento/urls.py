"""nasagente URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from casamento.views import list_casamento, send_message_telegram, choice_item

router = DefaultRouter()

urlpatterns = router.urls + [
    path("casamento_lista/", list_casamento, name="casamento_lista"),
    path("send_message/", send_message_telegram, name="send_message"),
    path("choice_item/", choice_item, name="choice_item"),
]