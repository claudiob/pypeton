import os.path
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

# Include apps on the path
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

MANAGERS = ADMINS = (
    ('Red Interactive', 'geeks@ff0000.com'),
)

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_ROOT = MEDIA_ROOT
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '%(SECRET)s'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
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
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'initial_data',      # to load fixtures
)
