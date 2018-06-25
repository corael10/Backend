from rest_framework.serializers import ModelSerializer

from apps.proveedor.models import Proveedor

class ProveedorSerializer(ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id','nombre','direccion','ciudad','telefono','saldo','fecha_registro')


 
       