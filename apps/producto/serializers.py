from rest_framework.serializers import ModelSerializer

from apps.producto.models import *
from apps.proveedor.serializers import *


class ProductoSerializerMarca(ModelSerializer):
    proveedor = ProveedorSerializer()
    class Meta:
        model = Marca
        fields = ('id','nombre','proveedor')

class ProductoSerializerMarcaPost(ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id','nombre','proveedor')        

class ProductoSerializerFamilia(ModelSerializer):
    #marca = ProductoSerializerMarca()
    class Meta:
        model = Familia
        fields = ('id','nombre','descripcion', 'marca','promoactiva')

        
class ProductoSerializer(ModelSerializer):
    marca = ProductoSerializerMarca()
    familia = ProductoSerializerFamilia()
   

    class Meta:
        model = Producto        
        fields = ('id','codigo','nombre','descripcion','marca','familia','precio_proveedor','precio_1','precio_2','precio_3','precio_promo','unidades') 

class ProductoSerializerPost(ModelSerializer):
    
    class Meta:
        model = Producto        
        fields = ('id','codigo','nombre','descripcion','marca','familia','precio_proveedor','precio_1','precio_2','precio_3','precio_promo','unidades') 




