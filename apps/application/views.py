from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from apps.application.models import *
from apps.application.serializers import *
from django.db.models import ProtectedError

# Create your views here.
class GetAppList(APIView):
    def get(self, request, format=None):
        lista = Application.objects.all()
        serializer = ApplicationSerializer(lista, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ApplicationSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            idApp= serializer.data['id']
            insert = Application.objects.all().filter(id=idApp)
            serializer2 = ApplicationSerializer(insert, many=True)  
            return Response(serializer2.data, status=status.HTTP_201_CREATED)
        return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)

class AppDetalle(APIView):
  
    def get_object(self, pk):
        try:
            return Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        app = self.get_object(pk)
        serializer = ApplicationSerializer(app)
        print(serializer.data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        app = self.get_object(pk)
        serializer = ApplicationSerializerPost(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        app = self.get_object(pk)
        try:
            app.delete()        
        except ProtectedError:
            error_message = "This object can't be deleted!!"
            return Response(error_message,status=status.HTTP_424_FAILED_DEPENDENCY)   
        return Response(status=status.HTTP_204_NO_CONTENT)   
        



      


class GetVersionAppList(APIView):
    def get(self, request, format=None):
        lista = VersionApp.objects.all()
        serializer = VersionAppSerializer(lista, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = VersionAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


class VersionAppDetalle(APIView):
  
    def get_object(self, pk):
        try:
            return VersionApp.objects.get(pk=pk)
        except VersionApp.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print(pk)
        versionapp = self.get_object(pk)
        serializer = VersionAppSerializer(versionapp)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        versionapp = self.get_object(pk)
        serializer = VersionAppSerializer(versionapp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        versionapp = self.get_object(pk)
        try:
            versionapp.delete()        
        except ProtectedError:
            error_message = "This object can't be deleted!!"
            return Response(error_message,status=status.HTTP_424_FAILED_DEPENDENCY)   
        return Response(status=status.HTTP_204_NO_CONTENT)   