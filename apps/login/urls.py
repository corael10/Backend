from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.login.views import *
urlpatterns = [ 
    #url(r'^login', login)
    url(r'^login/$', Login.as_view(), name='Login'),
    url(r'^logoyt/$', Logout.as_view(), name='Logout'),    
    url(r'^GetUserPassword/$', GetUserPassword.as_view(), name='GetUserPassword'),  
    url(r'^GetUserPassword/(?P<pk>[0-9]+)/$', GetUserPassword.as_view(),name='GetUserPassword'),

]

urlpatterns = format_suffix_patterns(urlpatterns)