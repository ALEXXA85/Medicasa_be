from dataclasses import fields
from rest_framework import serializers

from appMedi.models.diagnostico import Diagnostico

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = '__all__'