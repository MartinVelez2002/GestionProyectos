from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class Usuario(AbstractUser):
    cedula = models.CharField(max_length=10, default='', unique=True)
    
    groups = models.ForeignKey(
        Group,
        related_name='groupsUser', 
        blank=True,
        help_text='Rol de la persona',
        verbose_name='groups',
        on_delete=models.CASCADE,
        null=True,
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='permissionsUser',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def clean_cedula(self):
        cedula = self.cedula
        
        if not cedula.isdigit():
            raise ValidationError('La cédula debe contener solo datos numéricos.')
        

        if len(cedula) != 10:
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

    def clean(self):
        super().clean()
        # Validación adicional: Asegura que la cédula sea única
        if Usuario.objects.filter(cedula=self.cedula).exclude(pk=self.pk).exists():
            raise ValidationError({'cedula': 'Este número de cédula ya está registrado.'})

    def save(self, *args, **kwargs):
        # Encripta la contraseña antes de guardar
        if not self.pk or 'password' in kwargs:  # Si es un nuevo usuario o se cambió la contraseña
            self.password = make_password(self.password)
        super().save(*args, **kwargs)