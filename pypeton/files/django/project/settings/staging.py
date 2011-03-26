from settings import * 

# Include all the settings specific to 'staging' machines
# such as DATABASES, TIME_ZONE, DEFAULT_FILE_STORAGE
DEBUG = True 
DATABASES = {
    'default': {
        'NAME': '%(PROJECT_NAME)s_staging',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}
