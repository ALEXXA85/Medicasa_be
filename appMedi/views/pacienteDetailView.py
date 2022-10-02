from rest_framework import generics, status

from appMedi.models.paciente import Paciente
from appMedi.serializers.pacienteSerializer import PacienteSerializer

class PacienteDetailView(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)