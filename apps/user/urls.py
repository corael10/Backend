from django.conf.urls import url,include

from rest_framework.urlpatterns import format_suffix_patterns
from apps.user.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 
    
    url(r'^GetUser/$', GetUserList.as_view(), name='GetUser'),  
    url(r'^GetUser/(?P<pk>[0-9]+)/$', GetUserDetalle.as_view(),name='GetUserDetalle'),
    url(r'^upload/$', FileView.as_view(), name='file-upload'),
    url(r'^GetUserimg/$', GetUserimg.as_view(), name='GetUserimg'),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns = format_suffix_patterns(urlpatterns)