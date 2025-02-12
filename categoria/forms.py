from .models import Categoria
from django import forms

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'imagen']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'imagen': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }
        labels = {
            'nombre': 'Nombre de la categoria',
            'imagen': 'URL de Imagen de la categoria'
        }
        error_messages = {
            'nombre': {
                'required': 'El campo nombre es obligatorio'
            },
            'imagen': {
                'required': 'El campo imagen es obligatorio'
            }
        }