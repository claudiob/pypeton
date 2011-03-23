from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Homepage
    (r'^$', TemplateView.as_view(template_name='homepage.html'))
)

urlpatterns += staticfiles_urlpatterns()