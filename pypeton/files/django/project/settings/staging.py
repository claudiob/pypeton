from settings import * 

# Include all the settings specific to 'staging' machines
# such as DATABASES, TIME_ZONE, DEFAULT_FILE_STORAGE

DATABASES = {
    'default': {
        'NAME': '%(PROJECT_NAME)s_staging',
        'ENGINE': 'django.db.backends.mysql',
        'USER': '%(PROJECT_NAME)s_staging_user',
        'PASSWORD': '[set password here]',
        'HOST': 'localhost'
    }
}
