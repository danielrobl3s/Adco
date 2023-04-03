from rest_framework import serializers
from .models import ProjectClientes

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectClientes
        fields = '__all__'