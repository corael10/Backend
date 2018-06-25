from rest_framework.serializers import ModelSerializer

from apps.set.models import Chipset,HistVersion,Firmware
from apps.application.models import *
 

class VersionAppSerializer(ModelSerializer):
    
    class Meta:
        model = VersionApp
        fields =('id','version')


class ApplicationSerializer(ModelSerializer):
    version= VersionAppSerializer()
    class Meta:
        model = Application
        fields =('id','app_id','name','version')

class ApplicationSerializerPost(ModelSerializer):
    
    class Meta:
        model = Application
        fields =('id','app_id','name','version')        