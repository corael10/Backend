from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.shortcuts import render
import json
from rest_framework import status
from django.http import Http404
from apps.user.serializers import *


try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

class Login(APIView): 
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        print('user ',user)
        if not user:
            return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)
            
        token, _ = Token.objects.get_or_create(user=user)
        print(token.key)
        print(token.user_id)
        queryset = User.objects.raw('select * from auth_user where id= %s',[token.user_id])
        serializer  = UserSerializer(queryset,many=True)   
        #full_name = '%s %s' % (self.first_name, self.last_name)
        
        print(serializer.data)
       
        response_data={}
        response_data['token']= token.key
        response_data['user']=serializer.data
        print(response_data)
        return Response(response_data) 


class Logout(APIView):
    def post(self, request):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        logout(request)

        return Response({"success": _("Successfully logged out.")},
                     status=status.HTTP_200_OK)

class GetUserPassword(APIView):
  
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        print('user ',user)
        if not user:
            return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    def put(self, request, pk, format=None):
        username = request.data.get("usuario")
        password = request.data.get("password_anterior")
        user = authenticate(username=username, password=password)
        print('user ',user)
        if not user:
            return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

        #user = Productos_pedido_entrada.objects.all().filter(id=pk)
       
        user.set_password(request.data.get("password"))
        user.save()
        print(user.password)
        serializer = UserSerializer(user)
        print(serializer.data)

        return Response(serializer.data) 

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        try:
            user.delete()        
        except ProtectedError:
            error_message = "This object can't be deleted!!"
            return Response(error_message,status=status.HTTP_424_FAILED_DEPENDENCY)   
        return Response(status=status.HTTP_204_NO_CONTENT)             