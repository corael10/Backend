from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.pedido.views import *
urlpatterns = [ 
    
    url(r'^GetPedido/$', GetpedidoList.as_view(), name='GetpedidoList'),
    url(r'^GetPedido/(?P<pk>[0-9]+)/$', PedidoDetalle.as_view(),name='PedidoDetalle'),
    url(r'^MarcaPedido/$', MarcaPedido.as_view(), name='MarcaPedido'),
    url(r'^MarcaPedido/(?P<pk>[0-9]+)/$', MarcaPedido.as_view(),name='MarcaPedido'),
    url(r'^GetPedSelect/(?P<pk>[0-9]+)/$', GetPedSelect.as_view(),name='GetPedSelect'),
    url(r'^GetDetalleSelect/(?P<pk>[0-9]+)/$', GetDetalleSelect.as_view(),name='GetDetalleSelect'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)