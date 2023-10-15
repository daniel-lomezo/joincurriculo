from django.contrib import admin
from django.urls import path
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
