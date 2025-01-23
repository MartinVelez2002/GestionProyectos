from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Sprint(models.Model):
    Titulo = models.CharField(max_length=100, unique=True)
    Fecha_inicio = models.DateField(blank=True, null=False)
    Fecha_fin = models.DateField(blank=True, null=False)