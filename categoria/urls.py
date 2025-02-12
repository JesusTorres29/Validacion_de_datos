from django.urls import path
from .views import *

urlpatterns = [
    path('registro/', registrarCategoria, name='registrarCategoria'),
    path('api/get/', Lista_categorias, name='lista'),
    path('json/', json_categorias, name='json_categorias'),
    path('api/post/', registrar_Categoria, name='post'),
]