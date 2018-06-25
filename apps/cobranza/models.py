from django.db import models

from apps.cliente.models import *
from apps.empleado.models import *
# Create your models here.
from datetime import date 

     
class Cobranza_entrada (models.Model):
    cliente = models.ForeignKey(Cliente,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    empleado = models.ForeignKey(Empleado,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    fecha= models.DateField()     
    abono = models.IntegerField(blank=True, default=0) 
    total =  models.IntegerField(blank=True, default=0)
    status = models.BooleanField(default=False) 
    
    def __str__(self):
        return u'%s %s' % (self.id,self.cliente)





     
    
    