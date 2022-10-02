from dataclasses import fields
from rest_framework import serializers

from appMedi.models.historiaClinica import Historiaclinica

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historiaclinica
        fields = '__all__'