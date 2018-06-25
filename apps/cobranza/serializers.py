from rest_framework.serializers import ModelSerializer


from apps.cobranza.models import *
from apps.empleado.serializers import *
from apps.cliente.serializers import *


        

class CobranzaSerializer(ModelSerializer):
    cliente=ClienteSerializer()
    empleado=EmpleadoSerializer() 
    class Meta:
        model = Cobranza_entrada        
        fields = ('id','cliente','empleado','fecha','total','abono','status') 

class CobranzaSerializerPost(ModelSerializer):
    
    class Meta:
        model = Cobranza_entrada        
        fields = ('id','cliente','empleado','fecha','total','abono','status') 

