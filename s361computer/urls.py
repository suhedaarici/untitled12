__author__ = 'suhedaarici'

from django.conf.urls import patterns, include, url
from django.views.generic import ListView, TemplateView, DetailView
from .views import mysearch



urlpatterns = patterns('',
    url(r'^$',mysearch),
    url(r'^$', ListView.as_view(queryset=mysearch,template_name="base.html")),

)