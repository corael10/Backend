from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

#from apps.user.models import User
from apps.user.serializers import UserSerializer
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

    

# Create your views here.


class TestConnection(APIView):
        #serializer = ClienteSerializer
    
    def get_object(self, pk):
        print('pk' ,pk)
        try:
            Con = MySQLdb.Connect(host='105.102.15.72', port =3306, user='sqa_admin',passwd='adminsqa',database='ono')            
            cursor = Con.cursor()            
            var = cursor.callproc("ono.updateDays")
            Con.commit()             
            for result in cursor.fetchall():
                print(result)
        except Exception as e:
            print("Exeception occured:{}".format(e))
            
            
        finally:
            cursor.close()
            Con.close()


class GetUserDetalle(APIView):
  
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        #user = self.get_object(pk)
        print('user '+request.data)
        serializer = UserSerializer(user)
        print(serializer.data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        try:
            user.delete()        
        except ProtectedError:
            error_message = "This object can't be deleted!!"
            return Response(error_message,status=status.HTTP_424_FAILED_DEPENDENCY)   
        return Response(status=status.HTTP_204_NO_CONTENT)   
