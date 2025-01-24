from django.db import models
from Login.models import Usuario
# Create your models here.
class Proyecto(models.Model):
    Nombre = models.CharField(max_length=100, unique=True)
    Descripcion = models.CharField(max_length=200, )
    Fecha_inicio = models.DateField(auto_now=False)
    Fecha_fin = models.DateField(auto_now=False)
    Gerente = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='gerente')
    Cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='cliente')