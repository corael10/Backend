from django.db import models
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

from apps.project.models import Project 
from datetime import date 
# Create your models here.

class Firmware (models.Model):
    firmware= models.CharField(max_length=50)
    firmware_number = models.CharField(max_length=50,blank=True, null=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return u'%s %s' % (self.firmware,self.firmware_number)



        #chipset status model
class StatusPreotn(models.Model):    
    date_i = models.DateField()
    date_f = models.DateField()
    status =  models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    user = models.ForeignKey(User,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return u'%s %s' % (self.status,self.date_i)
 

class Chipset (models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50,blank=True, null=True)
    year = models.CharField(max_length=50,blank=True, null=True)
    firmware_set = models.ForeignKey(Firmware,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    ##firmware_number = models.ForeignKey(Firmware,null=True, blank=True)
    serie = models.CharField(max_length=50,blank=True, null=True) 
    infolink =models.CharField(max_length=50,blank=True, null=True)
    psid =models.CharField(max_length=50,blank=True, null=True) 
    url = models.TextField(blank=True, null=True)
    project=models.ForeignKey(Project,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    statuspreotn=models.ForeignKey(StatusPreotn,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    #statuspreotn = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return u'%s' % (self.name)


    
class HistVersion (models.Model):
    chipset= models.ForeignKey(Chipset,null=True, blank=True)
    firmware_set =models.ForeignKey(Firmware,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    ##firmware_number = models.ForeignKey(Firmware,related_name='tracks',null=True, blank=True)
    date = models.DateField()
    infolink = models.CharField(max_length=50,blank=True, null=True)
    user= models.ForeignKey(User,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return u'%s %s' % (self.firmware_set, self.date)  





class ChipsetStatusPreotn(models.Model):
    status = models.ForeignKey(StatusPreotn,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    chipset = models.ForeignKey(Chipset,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)
    firmware = models.ForeignKey(Firmware,related_name='%(class)s_requests_created',null=True, blank=True,on_delete=models.PROTECT)

    