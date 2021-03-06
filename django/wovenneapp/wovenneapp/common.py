DEBUG = False

TEMPLATES = {
    'TEMPLATE_DEBUG': False,
    'TEMPLATE_CONTEXT_PROCESSORS': (
        'django.template.context_processors.request',
        'django.template.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'django_facebook.context_processors.facebook',
    ),
    'TEMPLATE_LOADERS': [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',
    ]

}

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Extensions framework.
    'django_extensions',

    # Asset management.
    'pipeline',

    # Password resets.
    'password_reset',

    # Project apps
    'app',
    'wovenneapp',
    'pages',

    # Storage backends.
    'storages',

    # Facebook
    'django_facebook',
]

MIDDLEWARE_CLASSES = [
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'

ROOT_URLCONF = 'wovenneapp.urls'

STATIC_ROOT = '/var/www/wovenne.com/static/'
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_FINDERS = [
    # Default finders.
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]

MEDIA_ROOT = '/var/www/wovenne.com/media'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

# Pipeline (compression) settings.
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.UglifyJSCompressor'

# if TEMPLATE_DEBUG:
#     TEMPLATE_LOADERS = [
#         # Default values.
#         'django.template.loaders.filesystem.Loader',
#         'django.template.loaders.app_directories.Loader',
#
#         # Custom values.
#         'django.template.loaders.eggs.Loader',
#     ]
#
# else:
#     # Template loaders.
#     TEMPLATE_LOADERS = [
#         # Default values.
#         ('django.template.loaders.cached.Loader', (
#             'django.template.loaders.filesystem.Loader',
#             'django.template.loaders.app_directories.Loader',
#         )),
#
#         # Custom values.
#         'django.template.loaders.eggs.Loader',
#     ]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

from logging_settings import *
from pipeline_settings import *
from cache_settings import *
# from analytical_settings import *
