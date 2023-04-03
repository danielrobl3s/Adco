from rest_framework import serializers
from .models import ProjectMaterials

class materialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMaterials
        fields = '__all__'