from django.db import models
# from project_clientes import ProjectClientes

class ProjectGastos(models.Model):
    id_gasto = models.AutoField(primary_key=True)
    # id_proyecto = models.ForeignKey(ProjectClientes, models.DO_NOTHING, db_column='id_proyecto', to_field='id_proyecto')
    concepto = models.CharField(max_length=20, blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    metodo_pago = models.CharField(max_length=20, blank=True, null=True)
    cobrador = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:

        db_table = 'project_gastos'

        def __str__(self) -> str:
            return self.title