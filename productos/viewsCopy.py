from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse 
from .models import Producto
from .forms import ProductoForm
import json

#metodo que devuelva el json 
def Lista_productos(request):
    #obtener todas las instancias de la tabla
    productos = Producto.objects.all()
    #Construir una variable en formato de diccionario
    #porque el jsonResponse necesita un diccionario
    data = [
        {
            'nombre':producto.nombre,
            'precio':producto.precio,
            'imagen':producto.imagen
        }
        for producto in productos
    ]
    #devolver la respuesta en formato json
    return JsonResponse(data, safe=False)

def indexProductos(request):
    return render(request, 'homeProductos.html')

def registro(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro')
    else:
        form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})
#render recarga la pagina y redirige a la pagina que se le indique
#funcion que registre sin recargar la pagina sin utilizar el render 
def registrar_producto(request):
    if request.method == 'POST':
        try:
            #intentar obtener los datos del body del request
            data= json.loads(request.body)
            #crear una instancia del modelo Producto
            producto= Producto.objects.create(
                #basicamente es un constructor
                nombre=data['nombre'],
                precio=data['precio'],
                imagen=data['imagen']
            ) #la funcion create directamente ingresa el modelo a la base de datos
            return JsonResponse({'mensaje':'Producto creado exitosamente', 'id':producto.id}, status=201)
        except Exception as e:
            return JsonResponse({'error':str(e)}, status=400)
    return JsonResponse({'mensaje':'Metodo no soportado'}, status=405)

#metodo para actualizar un producto
def actualizar_producto(request, id_producto):
    if request.method == 'PUT':
        producto= get_object_or_404(Producto, id=id_producto)
        try:
            # producto= Producto.objects.get(id=id_producto)
            data= json.loads(request.body)
            producto.nombre= data('nombre', producto.nombre)
            producto.precio= data('precio', producto.precio)
            producto.imagen= data('imagen', producto.imagen)
            producto.save()
            return JsonResponse({'mensaje':'Producto actualizado exitosamente'}, status=200)
        except Exception as e:
            return JsonResponse({'Error':str(e)}, status=400)
    return JsonResponse({'Error':'Metodo no soportado'}, status=405)

#metodo para eliminar un producto
def eliminar_producto(request, id_producto):
    if request.method == 'DELETE':
        producto= get_object_or_404(Producto, id=id_producto)
        try:
            # producto= Producto.objects.get(id=id_producto)
            producto.delete()
            return JsonResponse({'mensaje':'Producto eliminado exitosamente'}, status=200)
        except Exception as e:
            return JsonResponse({'error':str(e)}, status=400)
    return JsonResponse({'Error':'Metodo no soportado'}, status=405)

#metodo que solo devuelva un objeto
def obtener__producto(request, id_producto):
    if request.method == 'GET':
        producto= get_object_or_404(Producto, id=id_producto)
        data= {
            'id':producto.id,
            'nombre':producto.nombre,
            'precio':producto.precio,
            'imagen':producto.imagen
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'Error':'Metodo no soportado'}, status=405)