from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.inventario.views import *
urlpatterns = [ 
    
    url(r'^GetInventario/$', GetInventarioList.as_view(), name='GetInventarioList'),
    url(r'^GetInventario/(?P<pk>[0-9]+)/$', InventarioDetalle.as_view(),name='InventarioDetalle'),
    url(r'^GetInvSelect/(?P<pk>[0-9]+)/$', GetInvSelect.as_view(),name='GetInvSelect'),
    url(r'^GetDetalleSelect/(?P<pk>[0-9]+)/$', GetDetalleSelect.as_view(),name='GetDetalleSelect'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)