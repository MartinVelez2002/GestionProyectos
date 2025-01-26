from django import forms
from .models import Usuario
from Gestion.forms_util import BaseForm
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class UsuarioForm(BaseForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repita la contraseña'}), label="Confirmar contraseña")  # Asegúrate de agregar este campo
    class Meta:
        model = Usuario
        fields = ['rol', 'username', 'first_name', 'last_name', 'password', 'cedula']
        widgets = {
            'password':forms.PasswordInput(attrs={'placeholder':'Ingrese una contraseña valida'}),
            'username':forms.TextInput(attrs={'placeholder':'Ingrese un nombre su usuario'}),
            'first_name': forms.TextInput(attrs={'placeholder':'Ingrese sus dos nombres'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Ingrese sus dos apellidos'}),
            'cedula': forms.NumberInput(attrs={'placeholder': 'Ingrese su cédula (XXXXXXXXX)'})
            }
        
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")

        return cleaned_data



class EditUsuarioForm(BaseForm):
    class Meta:
        model = Usuario
        fields = ['rol', 'username', 'first_name', 'last_name', 'cedula']