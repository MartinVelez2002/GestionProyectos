from django.db import models
from Proyecto.models import Proyecto


# Create your models here.
class Sprint(models.Model):
    Titulo = models.CharField(max_length=100, unique=True)
    Fecha_inicio = models.DateField(blank=True, null=False)
    Fecha_fin = models.DateField(blank=True, null=False)
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)

    def __str__(self):
        return self.Titulo