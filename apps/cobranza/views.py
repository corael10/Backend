import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from apps.cobranza.models import *
from apps.cliente.models import *
from apps.empleado.models import *

from apps.cobranza.serializers import *
from apps.cliente.serializers import *
from apps.empleado.serializers import *

from django.db.models import Max, Min, Avg

# Create your views here.



class CobranzaDetalle(APIView):
  
    def get_object(self, pk):
        try:
            return Cobranza_entrada.objects.get(pk=pk)
        except Cobranza_entrada.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print('request ')
        cobranza = Cobranza_entrada.objects.all().filter(cliente_id=pk).order_by('-id')
        serializer = CobranzaSerializer(cobranza, many=True)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        print(request.data)
        pedido = self.get_object(pk)
        try:
            request.data['proveedor']=request.data['proveedor']['id']
        except:
            request.data['proveedor']=request.data['proveedor']

        serializer = InventarioSerializerPost(inventario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cobranza = self.get_object(pk)
        cliente = Cliente.objects.get(id= cobranza.cliente_id) # obtenemos objeto cliente
        cliente.saldo = cliente.saldo + cobranza.abono
        cliente.save()
        cobranza.delete()         
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetCobranzaList(APIView):
    #serializer = ClienteSerializer
   
    def get(self, request, format=None):
        lista = Cobranza_entrada.objects.all().order_by('-id')
        serializer = CobranzaSerializer(lista, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        print('cobranz antes ',request.data)

        cliente = Cliente.objects.get(id= request.data['cliente']) # obtenemos objeto cliente
        
        cobranza_data = { #crea objeto para guardar en la tabla de pedidos el encabezado del pedido
                "cliente":request.data['cliente'],
                "fecha":request.data['fecha'],
                "empleado":request.data['empleado']['id'],
                "abono":request.data['abono'],
                "total":cliente.saldo - request.data['abono'],
            }       

        print('cobranza data ',cobranza_data)
        serializer = CobranzaSerializerPost(data=cobranza_data)
        if serializer.is_valid():
            serializer.save() #Guarda el objeto creando nuevo registro en la tabla 
            cliente.saldo = cliente.saldo - request.data['abono']
            #cliente.saldo = cobranza_data['total']
            cliente.save() #Guardamos la actualizacion con el nuevo saldo

            #updateEmpleado = Empleado.objects.get(id= pedido_data['empleado']) # Actualizamos el saldo en la tabla de Empleado
            #updateEmpleado.saldo = updateEmpleado.saldo + pedido_data['total']
            #updateEmpleado.save() #Guardamos la actualizacion con el nuevo saldo
          
            

            
            return Response(serializer.data, status=status.HTTP_201_CREATED)    

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 