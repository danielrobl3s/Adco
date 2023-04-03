from django.db import models

class Proyectos(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    proyecto = models.CharField(max_length=50, blank=True, null=True)
    institucion = models.CharField(max_length=20, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_termino = models.DateField(blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    ubicacion = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'proyectos'

        def __str__(self) -> str:
            return self.title