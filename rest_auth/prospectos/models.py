from django.db import models
from django.contrib.auth.models import User

class Prospectos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    observaciones = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'