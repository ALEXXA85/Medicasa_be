from dataclasses import fields
from rest_framework import serializers

from appMedi.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'