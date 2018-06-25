from django.contrib import admin
from apps.set.models import *
# Register your models here.


admin.site.register(Firmware)
admin.site.register(Chipset)
admin.site.register(HistVersion)