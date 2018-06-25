"""onoControl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^connection/', include('apps.connection.urls',namespace="connection")),
    url(r'^user/', include('apps.user.urls',namespace="user")),
    url(r'^Authentication/', include('apps.login.urls',namespace="login")),
    url(r'^empleado/', include('apps.empleado.urls',namespace="empleado")),
    url(r'^proveedor/', include('apps.proveedor.urls',namespace="proveedor")),
    url(r'^producto/', include('apps.producto.urls',namespace="producto")),
    url(r'^cliente/', include('apps.cliente.urls',namespace="cliente")), 
    url(r'^inventario/', include('apps.inventario.urls',namespace="inventario")),
    url(r'^pedido/', include('apps.pedido.urls',namespace="pedido")),
    url(r'^cobranza/', include('apps.cobranza.urls',namespace="cobranza")),
    url(r'^mensajes/', include('apps.mensajes.urls',namespace="mensajes")),
   # url(r'^apps/', include('apps.application.urls',namespace="apps")),
    

    
]
