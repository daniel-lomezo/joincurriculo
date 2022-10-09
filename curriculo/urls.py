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
from django.contrib import admin
from django.urls import path, include
from appcurriculo import urls as urls_curriculos
from casamento import urls as urls_casamento
from appcurriculo.views import redirecionamento


urlpatterns = [


    path('admin/', admin.site.urls),
    path("casamento/", include(urls_casamento)),
    path('curriculo/', include(urls_curriculos)),
   	path('', redirecionamento)
    

   
]
