from django.urls import path
from .views import *

urlpatterns = [
    path('', indexProductos, name='indexProductos'),
    path('api/get/', Lista_productos, name='lista'),
    path('registro/', registro, name='registro'),
    path('api/post/', registrar_producto, name='post'),
    path('api/put/', actualizar_producto, name='put'),
    path('api/delete/', eliminar_producto, name='delete'),
]