from rest_framework import serializers
from .models import Gastos

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gastos
        fields = '__all__'
