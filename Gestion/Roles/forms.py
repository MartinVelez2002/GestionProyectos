from django import forms
from django.contrib.auth.models import Group, Permission
from Gestion.forms_util import BaseForm
from django.core.exceptions import ValidationError

class RolesForm(BaseForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.SelectMultiple(),
        required=False
    )

    class Meta:
        model = Group
        fields = ['name', 'permissions']
    
    def clean_name(self):
        name = self.cleaned_data.get('name')  # Obtén el valor del campo 'name'
        
        # Validación 1: El nombre no puede estar vacío
        if not name:
            raise ValidationError('El nombre del rol no puede estar vacío.')
        
        # Validación 2: No se permiten números en el nombre
        if any(char.isdigit() for char in name):
            raise ValidationError('No se pueden agregar números al campo.')
        
        # Validación 3: El nombre del rol no debe existir previamente (excepto para la instancia actual)
        if self.instance.pk:  # Si estamos editando una instancia existente
            if Group.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Este nombre de rol ya existe.')
        else:  # Si estamos creando un nuevo rol
            if Group.objects.filter(name=name).exists():
                raise ValidationError('Este nombre de rol ya existe.')
        
        return name