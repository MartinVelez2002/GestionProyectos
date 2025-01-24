from django import forms
from .models import Usuario
from Gestion.forms_util import BaseForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password

class UsuarioForm(BaseForm):
    class Meta:
        model = Usuario
        fields = ['rol', 'username', 'first_name', 'last_name', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user