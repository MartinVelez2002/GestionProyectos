from django import forms
from .models import Proyecto
from Gestion.forms_util import BaseForm
from Login.models import Usuario

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Llama al __init__ de la clase padre
        # Filtra los usuarios con el rol de "Cliente"
        clientes = Usuario.objects.filter(rol__name='Cliente')
        gerente = Usuario.objects.filter(rol__name='Gerente')
        print("Usuarios filtrados:", clientes)  # Depuración
        self.fields['Cliente'].queryset = clientes
        self.fields['Gerente'].queryset = gerente