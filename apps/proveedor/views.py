import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from apps.proveedor.models import Proveedor
from apps.proveedor.serializers import ProveedorSerializer

# Create your views here.

class GetProveedorList(APIView):
    #serializer = ClienteSerializer
   
    def get(self, request, format=None):
        lista = Proveedor.objects.all()
        serializer = ProveedorSerializer(lista, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProveedorDetalle(APIView):
  
    def get_object(self, pk):
        try:
            return Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        proveedor = self.get_object(pk)
        serializer = ProveedorSerializer(proveedor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        proveedor = self.get_object(pk)
        serializer = ProveedorSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        proveedor = self.get_object(pk)
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)