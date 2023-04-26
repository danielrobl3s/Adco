from rest_framework import serializers
from .models import Materiales, Recursos

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiales
        fields = '__all__'