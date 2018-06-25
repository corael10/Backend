from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.empleado.views import GetEmpleadoList,GetEmpleadoDetalle 
urlpatterns = [ 
    
    url(r'^GetEmpleado/$', GetEmpleadoList.as_view(), name='GetEmpleado'),  
    url(r'^GetEmpleado/(?P<pk>[0-9]+)/$', GetEmpleadoDetalle.as_view(),name='GetEmpleadoDetalle'),

]

urlpatterns = format_suffix_patterns(urlpatterns)