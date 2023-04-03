from django.db import models
from project_clientes import ProjectClientes

class ProjectMaterials(models.Model):
    id_material = models.AutoField(primary_key=True)
    #id_proyecto = models.ForeignKey(ProjectClientes, models.DO_NOTHING, db_column='id_proyecto', to_field='id_proyecto')
    recurso = models.CharField(max_length=20, blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    concepto = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:

        db_table = 'project_materials'
        def __str__(self) -> str:
            return self.title