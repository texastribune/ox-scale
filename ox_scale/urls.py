from django.conf.urls import patterns, include, url
from django.contrib import admin
from ox_scale.apps.user_admin.admin import user_admin_site


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^crud/', include(user_admin_site.urls)),
    url('', include('ox_scale.apps.scale.urls', namespace='ox-scale')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
