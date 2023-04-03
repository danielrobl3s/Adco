from rest_framework import serializers
from .models import ProjectGastos

class project_gastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGastos
        fields = '__all__'