from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_control

from . import views


random_question = views.RandomQuestion.as_view()

urlpatterns = patterns('',
    url(r'^(?P<uuid>\w+)/$', cache_control(max_age=0)(random_question),
        name='random_question'),
    url(r'^(?P<uuid>\w+)/submit/$', views.question_response,
        name='question_response'),
)
