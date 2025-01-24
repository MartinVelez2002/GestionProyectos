from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'first_name', 'last_name', 'rol']  # Personaliza los campos a mostrar
    search_fields = ['username', 'rol']  # Puedes personalizar qué campos permitir para búsqueda


admin.site.register(Usuario, UsuarioAdmin)