from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.mensajes.models import Mensaje

 

class MensajeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    codeprod = serializers.CharField()
    nombreprod = serializers.CharField()
    mensaje = serializers.CharField()
    fecha = serializers.CharField()
    estatus = serializers.IntegerField()
    unidades = serializers.IntegerField()
