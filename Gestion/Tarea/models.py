from django.db import models
from Login.models import Usuario
from django.utils import timezone
Estado = (('P','Pendiente'),('E', 'En proceso'), ('F', 'Finaizado'))
# Create your models here.
class Tarea(models.Model):
    Titulo = models.CharField(max_length=100, unique=True)
    Descripcion = models.CharField(max_length=300)
    Estado = models.CharField(max_length=1, choices=Estado, default=Estado[0][0])
    Personal = models.ManyToManyField(Usuario)
    
    def __str__(self):
        # Obtener los nombres completos de los usuarios relacionados
        nombres_personal = [f"{usuario.first_name} {usuario.last_name}" for usuario in self.Personal.all()]
        # Unir los nombres en una cadena separada por comas
        return f"{self.Titulo} - Asignado a: {', '.join(nombres_personal)}"
    
    
class Comentario(models.Model):
    Personal = models.ForeignKey(Usuario, models.PROTECT)
    Tarea = models.ForeignKey(Tarea, models.PROTECT)
    Fecha_creacion = models.DateTimeField(default=timezone.now)
    Comentario = models.CharField(max_length=300)
    Estado = models.BooleanField(default=True)
    