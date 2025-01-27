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
        widgets = {
            'permissions': forms.Select(),
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')  # Obtén el valor del campo 'name'

        if not name:
            raise ValidationError('El nombre del rol no puede estar vacío.')

        if any(char.isdigit() for char in name):
            raise ValidationError('No se pueden agregar números al campo.')

        if self.instance.pk:
            if Group.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Este nombre de rol ya existe.')
        else:
            if Group.objects.filter(name=name).exists():
                raise ValidationError('Este nombre de rol ya existe.')
        return name