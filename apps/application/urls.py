from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.application.views import *
urlpatterns = [ 


    url(r'^GetApp/$', GetAppList.as_view(), name='GetChipset'),  
    url(r'^GetApp/(?P<pk>[0-9]+)/$', AppDetalle.as_view(),name='ChipsetDetalle'),   
    url(r'^GetVersionApp/$', GetVersionAppList.as_view(), name='GetChipset'),  
    url(r'^GetVersionApp/(?P<pk>[0-9]+)/$', VersionAppDetalle.as_view(),name='ChipsetDetalle'),     
    #url(r'^GetApp/', GetAppList.as_view(),name='GetApp'), 
    #url(r'^GetApp/(?P<pk>[0-9]+)/$',AppDetalle.as_view(),name='AppDetail'),
    #url(r'^GetVersionApp/', GetVersionAppList.as_view(),name='GetVersionApp'), 
    #url(r'^GetVersionApp/(?P<pk>[0-9]+)/$',VersionAppDetalle.as_view(),name='GetVersionApp'),  
]

urlpatterns = format_suffix_patterns(urlpatterns)