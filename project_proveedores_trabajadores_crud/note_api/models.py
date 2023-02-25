import uuid
from django.db import models

from django.db import models

class ProjectProveedoresTrabajadores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    especialidad = models.CharField(max_length=20, blank=True, null=True)
    concepto = models.CharField(max_length=20, blank=True, null=True)
    archivos = models.CharField(max_length=100, blank=True, null=True)
    contratos = models.CharField(max_length=50, blank=True, null=True)
    monto_contrato = models.FloatField(blank=True, null=True)
    abonos = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'project_proveedores_trabajadores'

        def __str__(self) -> str:
            return self.title
