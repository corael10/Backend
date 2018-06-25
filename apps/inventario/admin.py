from django.contrib import admin

from apps.inventario.models import *

# Register your models here.

admin.site.register(Inventario_entrada)
admin.site.register(Productos_inventario_entrada)  

