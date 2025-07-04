from django import forms 
from django.forms import ModelForm
from .models import *

class FormularioCurso(ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'inscriptos', 'solo_empresas', 'turno']

"""
        fields = ['nombre', 'inscriptos']
        labels = {
            'nombre': 'Nombre del Curso',
            'inscriptos': 'Cantidad de Inscriptos'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'inscriptos': forms.NumberInput(attrs={'class': 'form-control'})
        }
        help_texts = {
            'inscriptos': 'Ingrese la cantidad de inscriptos'
        }
        error_messages = {
            'nombre': {
                'required': 'Ingrese el nombre del curso'
            }
        }
"""        

"""
class FormularioCurso(forms.Form):
    nombre = forms.CharField(label="Curso", max_length=50)
    inscriptos = forms.IntegerField(label="Inscriptos")
    profesor = forms.CharField(max_length=50)
    solo_empresas = forms.BooleanField(label="Es para empresas", required=False)
    TURNOS = (
        ("M", "Mañana"),
        ("T", "Tarde"),
        ("N", "Noche")
    )
    turno = forms.ChoiceField(choices=TURNOS, required=True)
    fecha_inicio = forms.DateField(input_formats=["%d/%m/%Y"], label="Fecha de inicio")
    fecha_fin = forms.DateField(input_formats=["%d/%m/%Y"], label="Fecha de Fin")
    email = forms.EmailField(label="Correo Electronico", required=False)
"""    