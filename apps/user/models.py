from django.db import models
from apps.storage import OverwriteStorage

try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

class File(models.Model):
  file = models.FileField(storage=OverwriteStorage(),max_length=200 )
  nombre = models.CharField(max_length=150)
  usuario = models.ForeignKey(User,related_name='%(class)s_requests_created',null=True, blank=True)
  fecha = models.DateTimeField(auto_now_add=True)