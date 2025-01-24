from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class Usuario(AbstractUser):
    rol = models.ForeignKey(Group, on_delete=models.PROTECT, related_name='rol', null=True)
    cedula = models.CharField(max_length=10, default='')
    
    groups = models.ManyToManyField(
        Group,
        related_name='groupsUser', 
        blank=True,
        help_text='Rol de la persona',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='permissionsUser',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    
    def __str__(self):
        return self.username
    
    
