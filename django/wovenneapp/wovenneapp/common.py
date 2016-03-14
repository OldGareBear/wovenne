ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Asset management.
    'pipeline',

    # Password resets.
    'password_reset',

    'app',

    # Storage backends.
    'storages'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wovenneapp.urls'

STATIC_ROOT = '/var/www/wovenne.com/static/'
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_FINDERS = [
    # Default finders.
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finder'
]

MEDIA_ROOT = '/var/www/wovenne.com/media'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

# Pipeline (compression) settings.
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.UglifyJSCompressor'

if TEMPLATE_DEBUG:
    TEMPLATE_LOADERS = [
        # Default values.
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',

        # Custom values.
        'django.template.loaders.eggs.Loader',
    ]

else:
    # Template loaders.
    TEMPLATE_LOADERS = [
        # Default values.
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),

        # Custom values.
        'django.template.loaders.eggs.Loader',
    ]

from logging_settings import *
from analytical_settings import *
from pipeline_settings import *
from cache_settings import *