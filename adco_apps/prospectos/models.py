from django.db import models

class Prospectos(models.Model):
    id_prospecto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'prospectos'

        def __str__(self) -> str:
            return self.title