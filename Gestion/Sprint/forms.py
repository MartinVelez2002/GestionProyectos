from django import forms
from .models import Sprint
from Proyecto.models import Proyecto
from Tarea.models import Tarea
from Gestion.forms_util import BaseForm

class SprintForm(BaseForm):
    class Meta:
        model = Sprint
        fields = ['Titulo', 'Fecha_inicio', 'Fecha_fin', 'Proyecto', 'Tarea']
        widgets = {
            'Titulo': forms.TextInput(attrs={'placeholder': 'Ingrese el título del sprint'}),
            'Fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'Fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'Tarea': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
