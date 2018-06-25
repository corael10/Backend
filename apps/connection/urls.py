from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.connection.views import *
urlpatterns = [ 
    
    url(r'^Test/$', TestConnection.as_view(), name='TestConnectionL'),  
    url(r'^Test/(?P<pk>[0-9]+)/$', TestConnection.as_view(),name='TestConnection'),

]

urlpatterns = format_suffix_patterns(urlpatterns)