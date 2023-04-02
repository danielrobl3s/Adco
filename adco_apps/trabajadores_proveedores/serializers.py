from rest_framework import serializers
from .models import TrabajadoresProveedores

class trabajadores_pSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrabajadoresProveedores
        fields = '__all__'