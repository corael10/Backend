from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.mensajes.views import *
urlpatterns = [ 
    
    url(r'^GetMensaje/$', GetMensajeList.as_view(), name='GetMensajeList'),
    url(r'^GetMensaje/(?P<pk>[0-9]+)/$', MensajeDetalle.as_view(),name='MensajeDetalle'),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)