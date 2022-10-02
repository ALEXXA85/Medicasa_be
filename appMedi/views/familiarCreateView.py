from rest_framework import status, views
from rest_framework.response import Response

from appMedi.serializers.familiarSerializer import FamiliarSerializer

class FamiliarCreateView(views.APIView):
    def post(self,request,*args,**kwargs):
        serializer = FamiliarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data,status = status.HTTP_201_CREATED)