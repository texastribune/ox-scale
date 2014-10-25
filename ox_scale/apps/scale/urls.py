from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'(?P<uuid>\w+)/$', views.RandomQuestion.as_view(),
        name='random_question')
)
