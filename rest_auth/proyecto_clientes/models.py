from django.db import models
from django.contrib.auth.models import User

class Pclientes(models.Model):
    nombre = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=True)
    documentos = models.CharField(max_length=50)
    observaciones = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'proyecto_clientes'

    def __str__(self):
        return self.nombre