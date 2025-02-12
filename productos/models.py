from django.db import models

class proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class detalles_productos(models.Model):
    descripcion = models.TextField(max_length=400)
    fecha_caducidad = models.DateField()
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    detalles_producto = models.OneToOneField('detalles_productos',null= True, blank=True, on_delete=models.CASCADE)
    categoria = models.ForeignKey('categoria.Categoria',null= True, blank=True, on_delete=models.CASCADE)
    proveedor = models.ManyToManyField(proveedor, blank=True)
    def __str__(self):
        return self.nombre
    
from categoria.models import Categoria