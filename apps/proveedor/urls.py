from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.proveedor.views import GetProveedorList,ProveedorDetalle
urlpatterns = [ 
    
    url(r'^GetProveedor/$', GetProveedorList.as_view(), name='GetProveedor'),
    url(r'^GetProveedor/(?P<pk>[0-9]+)/$', ProveedorDetalle.as_view(),name='ProveedorDetalle'),
]

urlpatterns = format_suffix_patterns(urlpatterns)