from django.conf.urls.defaults import *
from models import Thing

urlpatterns = patterns('things.views',
    (r'^$', 'index'),
    (r'^(?P<thing_slug>.+)/$', 'show', {}, 'thing_detail'),
)

