from django.contrib import admin

from apps.producto.models import *

# Register your models here.

admin.site.register(Marca) 
admin.site.register(Familia)
admin.site.register(Producto)
