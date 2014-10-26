from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_control
from django.views.generic import TemplateView

from . import views


random_question = views.RandomQuestion.as_view()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^questions/(?P<uuid>\w+)/$', cache_control(max_age=0)(random_question),
        name='random_question'),
    url(r'^questions/(?P<uuid>\w+)/submit/$', views.question_response,
        name='question_response'),
)
