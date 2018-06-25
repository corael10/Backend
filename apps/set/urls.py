from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from apps.set.views import * #GetChipsetList,ChipsetDetalle,GetHistList,VersionHistorico,GetFirmwareList,GetFirmwareDetalle
urlpatterns = [ 
    
    url(r'^GetChipset/$', GetChipsetList.as_view(), name='GetChipset'),  
    url(r'^GetChipset/(?P<pk>[0-9]+)/$', ChipsetDetalle.as_view(),name='ChipsetDetalle'),
    url(r'^PostChipset/(?P<pk>[0-9]+)/$', ChipsetDetalle.as_view(),name='ChipsetDetalle'),    
    url(r'^GetChipset/GetFirmware/$', GetFirmwareList.as_view(), name='GetFirmwareList'),
    url(r'^GetChipset/GetFirmware/(?P<pk>[0-9]+)/$', GetFirmwareDetalle.as_view(), name='FirmwareDetalle'),    
    #url(r'^GetFirmware/$', GetFirmwareList.as_view(), name='GetFirmwareList'),
    url(r'^GetHist/$', GetHistList.as_view(), name='GetHistList'),
    url(r'^GetHist/(?P<pk>[0-9]+)/$', VersionHistorico.as_view(),name='GetHist'),
    url(r'^SetTimePREOTN/$', SetTimePREOTN.as_view(), name='SetTimePREOTN'),  
    url(r'^SetTimePREOTN/(?P<pk>[0-9]+)/$', SetTimePREOTN.as_view(),name='SetTimePREOTN'),
    

]

urlpatterns = format_suffix_patterns(urlpatterns)