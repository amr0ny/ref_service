import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('postgres_db'),
        'USER': os.getenv('postgres_user'),
        'PASSWORD': os.getenv('postgres_password'),
        'HOST': os.environ.get('postgres_host'),
        'PORT': os.getenv('postgres_port', 5432),
        'OPTIONS': {
            'options': '-c search_path=public,content'
        }
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
