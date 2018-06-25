from rest_framework.serializers import ModelSerializer

from apps.producto.models import *
from apps.inventario.models import *
from apps.producto.serializers import *
from apps.proveedor.serializers import *

#from drf_writable_nested import WritableNestedModelSerializer
        

class InventarioSerializer(ModelSerializer):
    proveedor=ProveedorSerializer()
    class Meta:
        model = Inventario_entrada        
        fields = ('id','folio','proveedor','fecha','fecha_proveedor','total') 

class InventarioSerializerPost(ModelSerializer):
    
    class Meta:
        model = Inventario_entrada        
        fields = ('id','folio','proveedor','fecha','fecha_proveedor','total') 


class Productos_inventario_entradaSerializer(ModelSerializer):
    producto=ProductoSerializer()
    inventario_entrada=InventarioSerializer()
    
    class Meta:
        model = Productos_inventario_entrada        
        fields = ('id','folio','producto','unidades','precio_proveedor','total','inventario_entrada') 

class Productos_inventario_entradaSerializerPost(ModelSerializer):
  
    
    class Meta:
        model = Productos_inventario_entrada        
        fields = ('id','folio','producto','unidades','precio_proveedor','total','inventario_entrada')         




