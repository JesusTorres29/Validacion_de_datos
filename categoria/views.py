from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Categoria
from .forms import CategoriaForm

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