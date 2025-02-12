from django.urls import path
from .viewsCopy import *

urlpatterns = [
    path('', indexProductos, name='indexProductos'),
    path('api/get/', Lista_productos, name='lista'),
    path('registro/', registro, name='registro'),
    path('api/post/', registrar_producto, name='post'),
    path('api/put/<str:id_producto>/', actualizar_producto, name='put'),
    path('api/delete/<str:id_producto>/', eliminar_producto, name='delete'),
    path('api/get/<str:id_producto>/', obtener__producto, name='get'),
]