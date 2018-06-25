from django.db import models
from apps.application import *
from datetime import date

# Create your models here.


class VersionApp(models.Model):    
    version = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return self.version


class Application(models.Model):
    app_id = models.IntegerField(blank=True)
    name = models.CharField(max_length=50, blank=True)
    version = models.ForeignKey(VersionApp,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name



        