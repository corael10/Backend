from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.cliente.views import *
urlpatterns = [ 
    
    url(r'^GetCliente/$', GetClienteList.as_view(), name='GetCliente'),
    url(r'^GetCliente/(?P<pk>[0-9]+)/$', GetClienteDetalle.as_view(),name='ClienteDetalle'),
    url(r'^GetEmpSelect/(?P<pk>[0-9]+)/$', GetEmpSelect.as_view(),name='GetEmpSelect'),
    url(r'^GetClienteMes/$', GetClienteMes.as_view(), name='GetClienteMes'),
    url(r'^GetClienteMes/(?P<pk>[0-9]+)/$', GetClienteMesRango.as_view(),name='GetClienteMesRango'),
    #url(r'^GetPrecio/(?P<pk>[0-9]+)/$', GetPrecio.as_view(), name='GetPrecio'),  
]

urlpatterns = format_suffix_patterns(urlpatterns) 