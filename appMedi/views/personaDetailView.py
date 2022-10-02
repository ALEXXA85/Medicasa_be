from rest_framework import generics, status

from appMedi.models.persona import Persona
from appMedi.serializers.personaSerializer import PersonaSerializer

class PersonaDetailView(generics.RetrieveAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)