from django.db import models
from apps.producto.models import *
from apps.proveedor.models import *
# Create your models here.
from datetime import date 

     
class Inventario_entrada (models.Model):
    proveedor = models.ForeignKey(Proveedor,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    folio= models.CharField(max_length=50,blank=True, null=True)
    fecha= models.DateField()
    fecha_proveedor =  models.DateField(default=date.today)   
    total =  models.IntegerField(blank=True, default=0) 
    
    def __str__(self):
        return u'%s' % (self.folio)

class Productos_inventario_entrada (models.Model):
    folio= models.CharField(max_length=50,blank=True, null=True)
    producto = models.ForeignKey(Producto,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT) 
    unidades= models.IntegerField(blank=True, default=0)
    precio_proveedor = models.IntegerField(blank=True, default=0)
    total = models.IntegerField(blank=True, default=0)
    inventario_entrada = models.ForeignKey(Inventario_entrada,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    

    def __str__(self):
         return u'%s %s' % (self.id,self.folio)



     
    
    