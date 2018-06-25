from rest_framework.serializers import ModelSerializer

from apps.empleado.models import Empleado

 

class EmpleadoSerializer(ModelSerializer):
    
    class Meta:
        model = Empleado
        fields =('id','nombre','apellido','direccion' , 'ciudad','saldo','telefono','fecha_contra','estatus')


