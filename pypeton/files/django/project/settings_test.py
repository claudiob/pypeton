from settings import * 

LETTUCE_APPS = ( # applications with lettuce features
    'things',
)
INSTALLED_APPS += (
    'lettuce.django',    # for Behavior Driven Development
    'adminlettuce' ,     # to generate documentation from features
    'radish',            # tests for admin
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': '%(PROJECT_NAME)s-test.db',
    }
}

# Store e-mail message in memory for testing
EMAIL_BACKEND = 'django.core.mail.backends.locmom.EmailBackend'
