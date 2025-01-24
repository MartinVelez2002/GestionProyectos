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

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        if Usuario.objects.filter(cedula=cedula).exists():
            raise ValidationError("Este número de cédula ya está registrado.")
        
        
        cedula = str(cedula)
        if not cedula.isdigit():
            raise ValidationError('La cédula debe contener solo datos numéricos.')
        longitud = len(cedula)
        if longitud != 10:
            raise ValidationError('Cantidad de dígitos incorrecta.')
        
        coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        total = 0
        
        for i in range(9):
            digito = int(cedula[i])
            coeficiente = coeficientes[i]
            producto = digito * coeficiente
            if producto > 9:
                producto -= 9
            total += producto
        
        digito_verificador = (total * 9) % 10
        if digito_verificador != int(cedula[9]):
            raise ValidationError('La cédula no es válida.')
        
        return cedula
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user