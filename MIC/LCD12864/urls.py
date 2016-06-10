from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect

from LCD12864.views import *

def auto_redirect(request):
    return HttpResponseRedirect('index/')

urlpatterns = patterns('',
    url(r'^$',auto_redirect),
    url(r'^index/$', index),
    url(r'^search/$', search),
    url(r'^update_database/$', update_database),
)