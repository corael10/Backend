from django.db import models
from apps.producto.models import *
from apps.proveedor.models import *
from apps.cliente.models import *
from apps.empleado.models import *
# Create your models here.
from datetime import date 


        
class Pedido_entrada (models.Model):
    cliente = models.ForeignKey(Cliente,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    empleado = models.ForeignKey(Empleado,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    empleadosustituto =  models.ForeignKey(Empleado,null=True, blank=True,on_delete=models.PROTECT) 
    fecha= models.DateField()     
    total =  models.IntegerField(blank=True, default=0) 
    estatus = models.BooleanField(default = False)
    
    def __str__(self):
        return u'%s %s' % (self.id,self.cliente)

class Productos_pedido_entrada (models.Model):
    producto = models.ForeignKey(Producto,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    unidades= models.IntegerField(blank=True, default=0)
    precio = models.IntegerField(blank=True, default=0)
    total = models.IntegerField(blank=True, default=0)
    pedido_entrada = models.ForeignKey(Pedido_entrada,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    

    def __str__(self):
        return u'%s' % (self.id)



     
    
    