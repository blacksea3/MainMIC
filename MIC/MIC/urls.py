from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import admin

admin.autodiscover()

def auto_redirect(request):
    return HttpResponseRedirect('backlearning/index')

#def auto_response(request):
#    print request
#    print request.GET
#    return HttpResponse('OK')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('LCD12864.urls')),
    #url(r'^$', auto_response),
)
