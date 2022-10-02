from rest_framework import generics, status

from appMedi.models.historiaClinica import Historiaclinica
from appMedi.serializers.historiaClinicaSerializer import HistoriaClinicaSerializer

class HistoriaclinicaDetailView(generics.RetrieveAPIView):
    queryset = Historiaclinica.objects.all()
    serializer_class =HistoriaClinicaSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)