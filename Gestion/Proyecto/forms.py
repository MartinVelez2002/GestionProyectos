from django import forms
from .models import Proyecto
from Gestion.forms_util import BaseForm

class ProyectoForm(BaseForm):
    class Meta:
        model = Proyecto
        fields = ['Nombre', 'Descripcion', 'Fecha_inicio', 'Fecha_fin', 'Gerente', 'Cliente']
        widgets = {
            'Nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del proyecto'}),
            'Descripcion': forms.Textarea(attrs={'placeholder': 'Ingrese la descripción del proyecto', 'rows': 3}),
            'Fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'Fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'Nombre': 'Nombre del Proyecto',
            'Descripcion': 'Descripción',
            'Fecha_inicio': 'Fecha de Inicio',
            'Fecha_fin': 'Fecha de Fin',
            'Gerente': 'Gerente del Proyecto',
            'Cliente': 'Clientes Asociados',
        }