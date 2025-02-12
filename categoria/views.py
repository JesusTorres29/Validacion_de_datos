from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Categoria
from .forms import CategoriaForm
import json

def registrarCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Categoria registrada')
    else:
        form = CategoriaForm()
    return render(request, 'registro_Categorias.html', {'form': form})

def Lista_categorias(request):
    categorias = Categoria.objects.all()
    data = [
        {
            'nombre':categoria.nombre,
            'imagen':categoria.imagen
        }
        for categoria in categorias
    ]
    return JsonResponse(data, safe=False)

def json_categorias(request):
    return render(request, 'categorias_cards.html')

#Crear categorias
def registrar_Categoria(request):
    if request.method == 'POST':
        try:
            #intentar obtener los datos del body del request
            data= json.loads(request.body)
            #crear una instancia del modelo Producto
            categoria= Categoria.objects.create(
                #basicamente es un constructor
                nombre=data['nombre'],
                imagen=data['imagen']
            ) #la funcion create directamente ingresa el modelo a la base de datos
            return JsonResponse({'mensaje':'Categoria creada exitosamente', 'id':categoria.id}, status=201)
        except Exception as e:
            return JsonResponse({'error':str(e)}, status=400)
    return JsonResponse({'mensaje':'Metodo no soportado'}, status=405)