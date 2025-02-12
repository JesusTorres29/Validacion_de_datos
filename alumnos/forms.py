from .models import Alumno
from django import forms

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre','apellido','edad','matricula','correo']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'id':'nombre',
                    'class':'form-control',
                    'placeholder':'Nombre del alumno'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'id':'apellido',
                    'class':'form-control',
                    'placeholder':'Apellido del alumno'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'id':'edad',
                    'class':'form-control',
                    'placeholder':'Edad del alumno'
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'id':'matricula',
                    'class':'form-control',
                    'placeholder':'Matricula del alumno',
                    # 'pattern':'^\d{5}[A-Za-z]{2}\d{3}$'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'id':'correo',
                    'class':'form-control',
                    'placeholder':'Correo del alumno'
                }
            )
        }