from django.db import models
class ProjectClientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    metodo_pago = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    documentos = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'project_clientes'

    def __str__(self) -> str:
        return self.nombre