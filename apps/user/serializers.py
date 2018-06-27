from rest_framework.serializers import ModelSerializer
from apps.user.models import *
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()



class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields =('id','username','first_name','last_name','email','last_login','is_superuser') 



class UserSerializerPost(ModelSerializer):
    
    class Meta:
        model = User
        fields =('id','username','first_name','last_name','email','date_joined','is_superuser','is_staff','is_active','password') 


class FileSerializer(ModelSerializer):
    
    class Meta():
        model = File
        fields = ('file', 'nombre', 'usuario','fecha')
