from rest_framework import generics, status

from appMedi.models.diagnostico import Diagnostico
from appMedi.serializers.diagnosticoSerializer import DiagnosticoSerializer

class DiagnosticoDetailView(generics.RetrieveAPIView):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)