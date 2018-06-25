from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

#from apps.user.models import User
from apps.empleado.serializers import EmpleadoSerializer
from apps.empleado.models import Empleado
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

# Create your views here.
class GetEmpleadoList(APIView):

    def get(self, request, format=None):
        lista = Empleado.objects.all()
        serializer = EmpleadoSerializer(lista, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetEmpleadoDetalle(APIView):
  
    def get_object(self, pk):
        try:
            return Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        empleado = self.get_object(pk)
        serializer = EmpleadoSerializer(empleado)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        empleado = self.get_object(pk)
        serializer = EmpleadoSerializer(empleado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print('delete')
        empleado = self.get_object(pk)
        try:
            empleado.delete()        
        except ProtectedError:
            error_message = "This object can't be deleted!!"
            return Response(error_message,status=status.HTTP_424_FAILED_DEPENDENCY)   
        return Response(status=status.HTTP_204_NO_CONTENT)   
