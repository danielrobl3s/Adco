from django.db import models
from proyectos.models import Proyecto
from django.contrib.auth.models import User
from trabajadores_proveedores.models import TrabajadoresProveedores

class Gastos(models.Model):
    concepto = models.CharField(max_length=50)
    monto = models.FloatField()
    metodo_pago = models.CharField(max_length=50)
    cobrador = models.ForeignKey(TrabajadoresProveedores, on_delete=models.CASCADE)
    fecha = models.DateField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'gastos'

    def __str__(self):
        return self.concepto