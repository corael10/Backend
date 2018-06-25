from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.producto.views import *
urlpatterns = [ 
    
    url(r'^GetProducto/$', GetProductoList.as_view(), name='GetProducto'),
    url(r'^GetProducto/(?P<pk>[0-9]+)/$', ProductoDetalle.as_view(),name='ProductoDetalle'),
    url(r'^UpdatePromo/(?P<pk>[0-9]+)/$', UpdatePromo.as_view(),name='UpdatePromo'),
    url(r'^GetMarca/$', GetMarca.as_view(), name='GetMarca'), 
    url(r'^getProv_Select/(?P<pk>[0-9]+)/$', getProv_Select.as_view(), name='getProv_Select'),
    url(r'^getMarc_Select/(?P<pk>[0-9]+)/$', getMarc_Select.as_view(), name='getMarc_Select'),
    url(r'^GetMarca/(?P<pk>[0-9]+)/$', GetMarca_detalle.as_view(), name='GetMarca_detalle'),
    url(r'^GetFamilia/$', GetFamilia.as_view(), name='GetFamilia'),  
    url(r'^GetFamilia_select/(?P<pk>[0-9]+)/$', getFamilia_Select.as_view(), name='getFamilia_Select'),
    url(r'^GetFamilia_Promocion/$', GetFamilia_Promocion.as_view(), name='GetFamilia_Promocion'),
    #url(r'^GetFamilia_Promocion/(?P<pk>[0-9]+)/$', GetFamilia_Promocion.as_view(), name='GetFamilia_Promocion'),
]

urlpatterns = format_suffix_patterns(urlpatterns)