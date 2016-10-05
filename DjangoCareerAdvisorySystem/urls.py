from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^careerquiz/', include('careerquiz.urls', namespace="careerquiz")),
    url(r'^careerchat/', include('careerchat.urls', namespace="careerchat")),
    url(r'^career/', include('career.urls', namespace="career")),
    url(r'^admin/', include(admin.site.urls)),
)
