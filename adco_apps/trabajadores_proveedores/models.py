from django.db import models

class TrabajadoresProveedores(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
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
        db_table = 'trabajadores_proveedores'

        def __str__(self) -> str:
            return self.title