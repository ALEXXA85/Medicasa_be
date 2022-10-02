from rest_framework import generics, status

from appMedi.models.signosVitales import Signosvitales
from appMedi.serializers.signosVitalesSerializer import SignosvitalesSerializer

class SignosvitalesDetailView(generics.RetrieveAPIView):
    queryset = Signosvitales.objects.all()
    serializer_class = SignosvitalesSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)