from rest_framework.serializers import ModelSerializer

from apps.producto.models import *
from apps.pedido.models import *
from apps.producto.serializers import *
from apps.empleado.serializers import *
from apps.cliente.serializers import *

#from drf_writable_nested import WritableNestedModelSerializer
        

class PedidoSerializer(ModelSerializer):
    cliente=ClienteSerializer()
    empleado=EmpleadoSerializer() 
    empleadosustituto=EmpleadoSerializer()
    class Meta:
        model = Pedido_entrada         
        fields = ('id','cliente','empleado','empleadosustituto', 'fecha','total','estatus') 

    

class PedidoSerializerPost(ModelSerializer):
    
    class Meta:
        model = Pedido_entrada         
        fields = ('id','cliente','empleado','empleadosustituto', 'fecha','total','estatus') 


class Productos_pedido_entradaSerializer(ModelSerializer):
    producto=ProductoSerializer()
    pedido_entrada=PedidoSerializer()
    
    class Meta:
        model = Productos_pedido_entrada        
        fields = ('id','producto','unidades','precio','total','pedido_entrada') 

class Productos_pedido_entradaSerializerPost(ModelSerializer):
  
    
    class Meta:
        model = Productos_pedido_entrada        
        fields = ('id','producto','unidades','precio','total','pedido_entrada') 




