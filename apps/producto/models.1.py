from django.db import models

# Create your models here.

class Marca (models.Model):
    nombre = models.CharField(max_length=50) 


class Familia (models.Model):
    nombre =  models.CharField(max_length=50)
    descripcion = models.TextField()   

class Producto (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()   
    familia = models.ForeignKey(Familia,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT))
    marca = models.ForeignKey(Marca,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT))
   # precio = models.ForeignKey(Precio,null=True, blank=True)


class Precio (models.Model):
     producto = models.ForeignKey(Producto,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT))
     tipo_precio = models.CharField(max_length=50)
     precio = models.IntegerField()
    