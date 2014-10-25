from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^questions/', include('ox_scale.apps.scale.urls', namespace='ox-scale')),
    url(r'^admin/', include(admin.site.urls)),
)
