from rest_framework import generics, status

from appMedi.models.personalMedico import Personalmedico
from appMedi.serializers.personalMedicoSerializer import PersonalmedicoSerializer

class PersonalmedicoDetailView(generics.RetrieveAPIView):
    queryset = Personalmedico.objects.all()
    serializer_class = PersonalmedicoSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)