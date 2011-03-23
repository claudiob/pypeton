from settings import * 

# Include all the settings specific to 'staging' machines
# such as DATABASES, TIME_ZONE, DEFAULT_FILE_STORAGE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(PROJECT_ROOT, '%(PROJECT_NAME)s_staging.db'),
    }
}
