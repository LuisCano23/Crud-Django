from django.contrib import admin
from django.urls import path
from Trabajos.Publicaciones.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal, name='home'),
    path('registro/', registro, name='registro'),
    path('publicaciones/', verpegas, name='publicaciones'),
    path('publicar/', publicar, name='publicar'),
    path('ingresar/', ingresar, name='ingresar'),
    path('salir/', salir, name='salir'),
    path('detalle/<int:publi_id>', detalle, name='detalle'),
    path('editar/<int:publi_id>', editar, name='editar'),
    path('borrar/<int:publi_id>', borrar, name='borrar')
]
