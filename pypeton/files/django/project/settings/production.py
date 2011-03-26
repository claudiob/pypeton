from settings import * 

# Include all the settings specific to 'production' machines
# such as DATABASES, TIME_ZONE
DEBUG = False
DATABASES = {
    'default': {
        'NAME': '%(PROJECT_NAME)s_production',
        'ENGINE': 'django.db.backends.mysql',
        'USER': '%(PROJECT_NAME)s_production_user',
        'PASSWORD': '[set password here]',
        'HOST': 'localhost'
    }
}
