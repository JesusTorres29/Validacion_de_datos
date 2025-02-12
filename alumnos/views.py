from .models import Alumno
from .serializers import AlumnoSerializer
from .forms import AlumnoForm
from django.shortcuts import render, redirect
from rest_framework import viewsets #vamos a crear una vistade varias al mismo tiempo
from rest_framework.renderers import JSONRenderer #renderiza los datos en formato JSON

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all() #obtiene todos los objetos de la base de datos
    serializer_class = AlumnoSerializer #serializa los objetos obtenidos
    renderer_classes = [JSONRenderer] #renderiza los datos en formato JSON

def index(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlumnoForm()
    return render(request, 'Alumnos.html', {'form':form})