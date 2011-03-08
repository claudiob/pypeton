from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Application           
    (r'^things/',         include('things.urls')),
    # Home-page
    (r'^$', 'things.views.index'),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns.insert(-2, url(r'^media/(?P<path>.*)',
        'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT}))