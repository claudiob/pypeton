import os.path
import sys
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Include apps on the path
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MANAGERS = ADMINS = (
    ('Red Interactive', 'geeks@ff0000.com'),
)

DATABASES = {
    'default': {
        # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(PROJECT_ROOT, '%(PROJECT_NAME)s.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
#SITE_ID = 1
USE_I18N = True
USE_L10N = True
#INTERNAL_IPS = ('127.0.0.1',) # Used for debug_toolbar

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '%(SECRET)s'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'initial_data',      # to load fixtures
    'things',
    #'debug_toolbar',
)

from socket import gethostname
hostname = gethostname().split('.')[0]

try:
    _f = __file__              
    path = os.path.join(PROJECT_ROOT, 'hosts')
    sys.path.insert(0, path)   
    globals().update(__import__(hostname).__dict__)
    sys.path.remove(path)      
    __file__ = _f              
except: 
    print >> sys.stderr, '%(yellow)sLocal settings file: [%(blue)shosts/%%s.py%(yellow)s] not found, skipped.%(normal)s' %% hostname

