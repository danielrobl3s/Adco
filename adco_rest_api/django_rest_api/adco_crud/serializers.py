from rest_framework import serializers
from .models import ProjectProveedoresTrabajadores

class ProjectProveedoresTrabajadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProveedoresTrabajadores
        fields = tuple(field.name for field in model._meta.fields)[1:]