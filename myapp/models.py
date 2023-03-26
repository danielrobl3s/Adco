from django.db import models

class Usuarios(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField(null=True, blank=True)
    posicion = models.CharField(max_length=255)
    telefono = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'public.usuarios'
