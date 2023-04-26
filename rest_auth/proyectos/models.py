from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    proyecto = models.CharField(max_length=50)
    institucion_empresa = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'proyectos'

    def __str__(self):
        return self.proyecto