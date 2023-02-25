from rest_framework import serializers
from .models import ProjectProveedoresTrabajadores

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProveedoresTrabajadores
        fields = '__all__'
