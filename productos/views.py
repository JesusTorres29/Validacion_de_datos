from .models import Producto
from django.shortcuts import render
from .forms import ProductoForm
from .serializers import ProductoSerializer
from rest_framework import viewsets #vamos a crear una vistade varias al mismo tiempo
from rest_framework.renderers import JSONRenderer #renderiza los datos en formato JSON
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all() #obtiene todos los objetos de la base de datos
    serializer_class = ProductoSerializer #serializa los objetos obtenidos
    renderer_classes = [JSONRenderer] #renderiza los datos en formato JSON

    #establecer metodos 
    #http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    
def agregar_prodcuto(request):
    form = ProductoForm(request.POST)
    return render(request, 'agregar.html', {'form': form})