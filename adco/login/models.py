from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)

    class Meta:
        db_table = 'usuarios'
        
        def __str__(self):
            return self.nombre