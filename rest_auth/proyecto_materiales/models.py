from django.db import models
from django.contrib.auth.models import User

class Proyecto_materiales(models.Model):
    recurso = models.CharField(max_length=50, null=True)
    cantidad = models.FloatField(default=0.00)
    concepto = models.TextField(null=True)
    fecha = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'proyecto_materiales'

    def __str__(self):
        return self.recurso