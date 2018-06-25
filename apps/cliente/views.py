from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

#from apps.user.models import User
from apps.cliente.serializers import *
from apps.cliente.models import *
from apps.cobranza.models import *
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

# Create your views here.
class GetClienteList(APIView):

    def get(self, request, format=None):
        lista = Cliente.objects.all()
        serializer = ClienteSerializer(lista, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = ClienteSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetClienteDetalle(APIView):
  
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        #print(request.data)
        cliente = self.get_object(pk)

        cliente_data = {
                    "id":request.data['id'],
                    "nombre":request.data['nombre'],
                    "apellido":request.data['apellido'],  
                    "ciudad":request.data['ciudad'],                    
                    "telefono":request.data['telefono'],
                    "saldo":request.data['saldo'],
                    "fecha_registro":request.data['fecha_registro'],
                    "empleado":request.data['empleado']
                    
                }
        print(cliente_data)        
        serializer = ClienteSerializerPost(cliente, data=cliente_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print('delete')
        cliente = self.get_object(pk)
        try:
            cliente.delete()        
        except ProtectedError:
            error_message = "This object can't be deleted!!"
            return Response(error_message,status=status.HTTP_424_FAILED_DEPENDENCY)   
        return Response(status=status.HTTP_204_NO_CONTENT)   



class GetEmpSelect(APIView):
  
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        #cliente = self.get_object(pk)
        cliente = Cliente.objects.all().filter(empleado=pk)
        serializer = ClienteSerializer(cliente,many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        #print(request.data)
        cliente = self.get_object(pk)

        cliente_data = {
                    "id":request.data['id'],
                    "nombre":request.data['nombre'],
                    "apellido":request.data['apellido'],  
                    "ciudad":request.data['ciudad'],                    
                    "telefono":request.data['telefono'],
                    "saldo":request.data['saldo'],
                    "fecha_registro":request.data['fecha_registro'],
                    "empleado":request.data['empleado']
                    
                }
        print(cliente_data)        
        serializer = ClienteSerializerPost(cliente, data=cliente_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print('delete')
        cliente = self.get_object(pk)
        try:
            cliente.delete()        
        except ProtectedError:
            error_message = "This object can't be deleted!!"
            return Response(error_message,status=status.HTTP_424_FAILED_DEPENDENCY)   
        return Response(status=status.HTTP_204_NO_CONTENT)   


class GetClienteMes(APIView):

    def get(self, request, format=None):
        queryset = Cobranza_entrada.objects.raw('SELECT a.id, b.cliente_id,b.empleado_id,b.abono,b.fecha FROM evo.cliente_cliente a, evo.cobranza_cobranza_entrada b '
        'where  b.cliente_id = a.id  and  b.fecha not between date_sub(now(), interval 2 week) and curdate() '
        'group by b.cliente_id, a.nombre ')
        #queryset = Cobranza_entrada.objects.raw('SELECT a.id, sum(b.abono) as total_abono, b.cliente_id,b.empleado_id FROM evo.cliente_cliente a, evo.cobranza_cobranza_entrada b where  b.cliente_id = a.id  and MONTH(b.fecha) = MONTH(CURRENT_DATE())'
        #'AND YEAR(b.fecha) = YEAR(CURRENT_DATE()) group by b.cliente_id, a.nombre order by total_abono DESC') //query para encontrar los mejores clientes del mes
        serializer = ClienteMesSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClienteSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     


class GetClienteMesRango(APIView):
  
    def get_object(self, pk):
        try:
            return Cobranza_entrada.objects.get(pk=pk)
        except Cobranza_entrada.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print('request ', request.data['fechaD'])
        print(' pk ',pk)
        fechaD = request.data['fechaD']
        fechaA = request.data['fechaA']
        queryset = Cobranza_entrada.objects.raw('SELECT a.id, sum(b.abono) as total_abono, b.cliente_id,b.empleado_id FROM evo.cliente_cliente a, evo.cobranza_cobranza_entrada b where  b.cliente_id = a.id  '
        ' and  b.fecha between %s and %s group by b.cliente_id, a.nombre order by total_abono DESC',[fechaD,fechaA])
        serializer = ClienteMesSerializer(queryset, many=True)
        return Response(serializer.data)


    def put(self, request, pk, format=None):        
        fechaD = request.data['fechaD']
        fechaA = request.data['fechaA']
        queryset = Cobranza_entrada.objects.raw('SELECT a.id, sum(b.abono) as total_abono, b.cliente_id,b.empleado_id FROM evo.cliente_cliente a, evo.cobranza_cobranza_entrada b where  b.cliente_id = a.id  '
        ' and  b.fecha between %s and %s group by b.cliente_id, a.nombre order by total_abono DESC',[fechaD,fechaA])
        serializer = ClienteMesSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)      

    
       