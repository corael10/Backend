from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.cobranza.views import * 
urlpatterns = [ 
    
    url(r'^GetCobranza/$', GetCobranzaList.as_view(), name='GetCobranzaList'),
    url(r'^GetCobranza/(?P<pk>[0-9]+)/$', CobranzaDetalle.as_view(),name='CobranzaDetalle'),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)