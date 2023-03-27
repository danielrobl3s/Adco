from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=True)
    documentos = models.CharField(max_length=70)
    observaciones = models.CharField(max_length=100)
    
    
    class Meta:
        db_table = 'clientes'