from settings import * 

# Include all the settings specific to machines set up to run test suites
# such as DATABASES, EMAIL_BACKEND, LETTUCE_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'test.db',
    }
}

# Store e-mail message in memory for testig
EMAIL_BACKEND = 'django.core.mail.backends.locmom.EmailBackend'

# Prevent interactive question about wanting a superuser created
# since the admin/admin user is already created through the initial data
# (taken from http://stackoverflow.com/questions/1466827/)
from django.db.models import signals
from django.contrib.auth.management import create_superuser
from django.contrib.auth import models as auth_app
signals.post_syncdb.disconnect(create_superuser, sender=auth_app,
    dispatch_uid = "django.contrib.auth.management.create_superuser")
