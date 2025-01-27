from django import forms
from .models import Tarea, Comentario
from Login.models import Usuario
from Gestion.forms_util import BaseForm


class TareaForm(BaseForm):
    class Meta:
        model = Tarea
        fields = ['Titulo', 'Descripcion', 'Estado', 'Personal', 'Sprint']
        widgets = {
            'Titulo': forms.TextInput(attrs={'placeholder': 'Ingrese el título de la tarea'}),
            'Descripcion': forms.Textarea(attrs={'placeholder': 'Ingrese la descripción de la tarea', 'rows': 3}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            Miembro = Usuario.objects.filter(groups__name='Miembro')

            self.fields['Personal'].queryset = Miembro

        
        
class ComentarioForm(BaseForm):
    class Meta:
        model = Comentario
        fields = ['Comentario']
        widgets = {
            'Comentario': forms.Textarea(attrs={'placeholder': 'Escriba su comentario', 'rows': 3}),
        }
