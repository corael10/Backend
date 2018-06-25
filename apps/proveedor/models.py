from django.db import models

# Create your models here.


class Proveedor (models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.TextField()  
    ciudad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    saldo = models.IntegerField()  
    fecha_registro = models.DateField()

    def __str__(self):
        return u'%s' % (self.nombre)
       
    