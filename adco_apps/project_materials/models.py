from django.db import models
from project_clientes.models import ProjectClientes

# class ProjectMaterials(models.Model):
#     id_material = models.AutoField(primary_key=True)
#     id_proyecto = models.AutoField(unique=True)
#     recurso = models.CharField(max_length=20, blank=True, null=True)
#     cantidad = models.FloatField(blank=True, null=True)
#     concepto = models.CharField(max_length=20, blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)

#     class Meta:

#         db_table = 'project_materials'
#         def __str__(self) -> str:
#             return self.title

class ProjectMaterials(models.Model):
    id_material = models.AutoField(primary_key=True)
    id_proyecto = models.ForeignKey(ProjectClientes, on_delete=models.CASCADE, default=0)
    recurso = models.CharField(max_length=20, blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    concepto = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'project_materials'

    def __str__(self) -> str:
        return self.concepto