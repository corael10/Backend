from django.db import models

     
class Mensaje (models.Model):  
    codeprod =  models.CharField(max_length=50,blank=True, null=True) 
    nombreprod =  models.CharField(max_length=50,blank=True, null=True)
    mensaje = models.CharField(max_length=150,blank=True, null=True)
    fecha= models.DateField()     
    estatus =  models.IntegerField(blank=True, default=0) 
    unidades =  models.IntegerField(blank=True, default=0) 
    
    def __str__(self):
        return u'%s' % (self.id)



     
    
    