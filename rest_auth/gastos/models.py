from django.db import models
from django.contrib.auth.models import User

class Gastos(models.Model):
    concepto = models.CharField(max_length=50)
    monto = models.FloatField()
    metodo_pago = models.CharField(max_length=50)
    cobrador = models.CharField(max_length=50)
    fecha = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'gastos'

    def __str__(self):
        return self.concepto