from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

#from apps.user.models import User
from apps.mensajes.serializers import *
from apps.mensajes.models import *
import mysql.connector  
import MySQLdb
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

# Create your views here.
class GetMensajeList(APIView):

    def get(self, request, format=None):
       
        try:
            Con = MySQLdb.Connect(host='localhost', port =3306, user='root',passwd='adminadmin',database='evo')            
            cursor = Con.cursor()            
            var = cursor.callproc("evo.creaMensaje")
            Con.commit()             
            for result in cursor.fetchall():
                print(result) 

        except Exception as e:
            print("Exeception occured:{}".format(e))            
            
        finally:
            cursor.close()
            Con.close()

        lista = Mensaje.objects.all()
        serializer = MensajeSerializer(lista, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MensajeDetalle(APIView):
  
    def get_object(self, pk):
        try:
            return Mensaje.objects.get(pk=pk)
        except Mensaje.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        mensaje = self.get_object(pk)
        serializer = MensajeSerializer(mensaje)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        mensaje = self.get_object(pk)
        serializer = MensajeSerializer(mensaje, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print('delete')
        mensaje = self.get_object(pk)
        try:
            mensaje.delete()        
        except ProtectedError:
            error_message = "This object can't be deleted!!"
            return Response(error_message,status=status.HTTP_424_FAILED_DEPENDENCY)   
        return Response(status=status.HTTP_204_NO_CONTENT)   
