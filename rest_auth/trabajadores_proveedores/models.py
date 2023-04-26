from django.db import models
from django.contrib.auth.models import User

class TrabajadoresProveedores(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    direccion = models.TextField()
    especialidad = models.CharField(max_length=100)
    concepto = models.TextField()
    archivos = models.TextField()
    contratos = models.TextField()
    monto_contrato = models.FloatField()
    abonos = models.FloatField()
    saldo = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    
    def __str__(self):
        return self.nombre






