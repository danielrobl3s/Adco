from rest_framework import serializers
from .models import Prospectos

class ProspectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prospectos
        fields = '__all__'