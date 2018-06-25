from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.user.views import GetUserList,GetUserDetalle 
urlpatterns = [ 
    
    url(r'^GetUser/$', GetUserList.as_view(), name='GetUser'),  
    url(r'^GetUser/(?P<pk>[0-9]+)/$', GetUserDetalle.as_view(),name='GetUserDetalle'),

]

urlpatterns = format_suffix_patterns(urlpatterns)