from rest_framework.serializers import ModelSerializer

from apps.set.models import *
from apps.user.serializers import UserSerializer



class FirmwareSerializer(ModelSerializer):
    class Meta:
        model = Firmware
        fields= ('id','firmware','firmware_number','date')
        
class StatusPreotnSerializer(ModelSerializer):  
       class Meta:
        model = StatusPreotn 
        fields = ('id','date_i','date_f','status','user')

class ChipsetSerializer(ModelSerializer):
    firmware_set=FirmwareSerializer()
    statuspreotn=StatusPreotnSerializer()
    class Meta:
        model = Chipset 
        fields = ('id','name','model','year','firmware_set','serie','infolink','psid','url','statuspreotn')

class ChipsetSerializerPost(ModelSerializer):
    class Meta:
        model = Chipset 
        fields = ('id','name','model','year','serie','infolink','psid','url','statuspreotn')
        

class ChipsetSerializerUpdate(ModelSerializer):
    class Meta:
        model = Chipset 
        fields = ('firmware_set')    
            

class HistSerializer(ModelSerializer):
    firmware_set=FirmwareSerializer()
    user=UserSerializer()
    chipset=ChipsetSerializer()

    class Meta:
        model = HistVersion 
        fields = ('id','chipset','firmware_set','infolink','date','user')

class HistSerializerPost(ModelSerializer):   
    class Meta:
        model = HistVersion 
        fields = ('id','chipset','firmware_set','infolink','date','user')

   



        

   

      
