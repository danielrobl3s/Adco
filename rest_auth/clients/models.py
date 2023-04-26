from django.db import models
from proyectos.models import Proyecto
from prospectos.models import Prospectos
from django.contrib.auth.models import User

class Clientes(models.Model):
    nombre = models.ForeignKey(Prospectos, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=True)
    documentos = models.CharField(max_length=50)
    observaciones = models.TextField(blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return self.nombre
