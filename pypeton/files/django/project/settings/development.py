from settings import * 

# Include all the settings specific to 'development' machines
# such as DATABASES, TIME_ZONE
DEBUG = True
TEMPLATE_DEBUG = DEBUG
TIME_ZONE = 'America/Los_Angeles'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(PROJECT_ROOT, '%(PROJECT_NAME)s_development.db'),
    }
}


# Load host-specific configuration file from hosts/[hostname].py
from socket import gethostname # Hostname based local settings 
hostname = gethostname().split('.')[0]
try:
    _f = __file__              
    path = os.path.join(PROJECT_ROOT, 'hosts')
    sys.path.insert(0, path)   
    globals().update(__import__(hostname).__dict__)
    sys.path.remove(path)      
    __file__ = _f              
except ImportError, e: 
    print >> sys.stderr, '%(yellow)sLocal settings file: [%(blue)shosts/%%s.py%(yellow)s] error:%(normal)s\n%%s' %% (hostname,e)


# Prevent interactive question about wanting a superuser created
# since the admin/admin user is already created through the initial data
# (taken from http://stackoverflow.com/questions/1466827/)
from django.db.models import signals
from django.contrib.auth.management import create_superuser
from django.contrib.auth import models as auth_app
signals.post_syncdb.disconnect(create_superuser, sender=auth_app,
    dispatch_uid = "django.contrib.auth.management.create_superuser")
