from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.cliente.models import *
from apps.empleado.serializers import *
from apps.cobranza.models import *
 

class ClienteSerializer(ModelSerializer):
    empleado = EmpleadoSerializer()
    class Meta:
        model = Cliente
        fields =('id','nombre','apellido','direccion' , 'ciudad','saldo','telefono','fecha_registro','estatus','empleado')


class ClienteSerializerPost(ModelSerializer):
   
    class Meta:
        model = Cliente
        fields =('id','nombre','apellido','direccion' , 'ciudad','saldo','telefono','fecha_registro','estatus','empleado')


class ClienteMesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cliente = ClienteSerializer()
    empleado = EmpleadoSerializer()
    fecha = serializers.DateField()
    abono =serializers.IntegerField()


        


