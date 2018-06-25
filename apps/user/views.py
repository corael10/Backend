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


class GetUserList(APIView):
    #serializer = ClienteSerializer
   
    def get(self, request, format=None):
        queryset = User.objects.raw('select * from auth_user')
        #queryset = User.objects.raw('select u.id, u.username, u.first_name, u.last_name, u.email, p.project_id '
        #'from auth_user as u left join  project_projectuser as p on u.id = p.user_id;')
        serializer  = UserSerializer(queryset,many=True) 


        return Response(serializer.data) 


    def post(self, request, format=None):
        

        username=request.data['username']
        
        last_name = request.data['last_name']
        is_superuser = request.data['is_superuser']
        email = request.data['username']+'@evoluxion.com'
        is_staff = request.data['is_superuser']
        is_active = 1
        date_joined = request.data['date_joined']
        password = 'evoluxion2018'

        user = User.objects.create_user(username,email,password)
        user.save()
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.is_superuser = request.data['is_superuser']
        user.is_staff = request.data['is_superuser']
        user.date_joined = request.data['date_joined']
        user.save() 

        return Response('Created User', status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
