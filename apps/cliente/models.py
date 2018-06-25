from django.db import models
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

from apps.empleado.models import *
from datetime import date 
# Create your models here.

class Cliente (models.Model):
    nombre= models.CharField(max_length=50)
    apellido = models.CharField(max_length=50,blank=True, null=True)
    direccion = models.CharField(max_length=50,blank=True, null=True)
    ciudad = models.CharField(max_length=50,blank=True, null=True)
    saldo = models.IntegerField(blank=True)
    telefono = models.CharField(max_length=50,blank=True, null=True)
    fecha_registro = models.DateField(default=date.today)
    estatus =  models.PositiveSmallIntegerField(default=0, blank=True, null=True) 
    empleado= models.ForeignKey(Empleado,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    def __str__(self):
        return u'%s %s' % (self.nombre,self.apellido)



    