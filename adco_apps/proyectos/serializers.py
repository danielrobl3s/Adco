from rest_framework import serializers
from .models import Proyectos

class proyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = '__all__'