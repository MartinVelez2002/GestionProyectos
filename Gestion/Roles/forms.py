from django import forms
from django.contrib.auth.models import Group
from Gestion.forms_util import BaseForm
from django.core.exceptions import ValidationError

class RolesForm(BaseForm):
    class Meta:
        model = Group
        fields = ['name']
    
    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        
        if not name:
            raise ValidationError('El nombre del rol no puede estar vacío.')
        
        if any(char.isdigit() for char in name):
            raise ValidationError('No se pueden agregar números al campo')
        
        if Group.objects.filter(name=name).exists():
            raise ValidationError('Este nombre de rol ya existe.')
        
        if Group.objects.filter(name=name).exists():
            raise ValidationError('Este nombre de rol ya existe.')