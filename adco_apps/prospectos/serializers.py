from rest_framework import serializers
from .models import Prospectos

class prospectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prospectos
        fields = '__all__'