from django.conf.urls import patterns, include, url
 
from careerchat import views
 
urlpatterns = patterns('',
        url(r'^$', views.index, name='basechat'),
	url(r'^testajax/$', views.testajax),
	
)
