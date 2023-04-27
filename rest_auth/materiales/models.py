from django.db import models
from proyectos.models import Proyecto
from django.contrib.auth.models import User
    
class Recursos(models.Model):
    nombre = models.CharField(max_length=50, default="nombre_recurso")
    tipo = models.CharField(max_length=50, default="estructural")
    precio = models.FloatField(default=0.00)
    unidad = models.CharField(max_length=50, default="Kilogramos")
    marca = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        db_table = 'recursos'

    def __str__(self):
        return self.nombre
    
class Materiales(models.Model):
    recurso = models.ForeignKey(Recursos, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.FloatField(default=0.00)
    total = models.FloatField(default=0.00)
    concepto = models.TextField(null=True)
    fecha = models.DateField(auto_now=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'materiales'

    def __str__(self):
        return self.recurso
    
    def save(self, *args, **kwargs):
        if self.recurso:
            self.total = self.recurso.precio * self.cantidad
        else:
            self.total = 0
        super(Materiales, self).save(*args, **kwargs)