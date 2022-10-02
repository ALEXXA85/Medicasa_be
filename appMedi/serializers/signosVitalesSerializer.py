from dataclasses import fields
from rest_framework import serializers

from appMedi.models.signosVitales import Signosvitales

class SignosvitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signosvitales
        fields = '__all__'