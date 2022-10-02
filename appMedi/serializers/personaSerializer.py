from dataclasses import fields
from rest_framework import serializers

from appMedi.models.persona import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('nombres','apellidos', 'telefono','genero')

    def insertPersona(self,validated_data):
        personaInstance = Persona.objects.create(**validated_data)
        return personaInstance  
    
    def getPersona(self,obj):
        persona = Persona.objects.get(id = obj.id)
        return {
            'id': persona.id,
            'nombres':persona.nombres,
            'apellidos':persona.apellidos,
            'telefono':persona.telefono,
            'genero':persona.genero,
        }