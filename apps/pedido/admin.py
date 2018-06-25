from django.contrib import admin

from apps.pedido.models import *

# Register your models here.

admin.site.register(Pedido_entrada)
admin.site.register(Productos_pedido_entrada)  

