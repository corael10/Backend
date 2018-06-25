from django.db import models
from apps.proveedor.models import Proveedor
# Create your models here.

class Marca (models.Model):
    nombre = models.CharField(max_length=50) 
    proveedor= models.ForeignKey(Proveedor,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return u'%s' % (self.nombre)



class Familia (models.Model):
    nombre =  models.CharField(max_length=50)
    descripcion = models.TextField()  
    marca =  models.ForeignKey(Marca,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    promoactiva = models.BooleanField(default=False)

    def __str__(self):
        return u'%s' % (self.nombre)    


class Producto (models.Model):
    codigo = models.CharField(max_length=50,default=0)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()   
    familia = models.ForeignKey(Familia,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    precio_proveedor= models.IntegerField(blank=True, default=0)
    precio_1= models.IntegerField(blank=True, default=0)
    precio_2= models.IntegerField(blank=True,default=0)
    precio_3= models.IntegerField(blank=True,default=0)
    precio_promo= models.IntegerField(blank=True,default=0)
    unidades= models.IntegerField(blank=True,default=0)


    def __str__(self):
        return u'%s' % (self.codigo)



     
    