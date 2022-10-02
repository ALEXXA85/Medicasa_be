from dataclasses import fields
from rest_framework import serializers

from appMedi.models.personalMedico import Personalmedico

class PersonalmedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalmedico
        fields = '__all__'