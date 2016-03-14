import os
import sys
import logging.config
from logging.handlers import SysLogHandler

# Logging Configuration
#
# See: http://stackoverflow.com/questions/20282521/django-request-logger-not-propagated-to-root/22336174#22336174
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stderr,
            'formatter': 'verbose'
        },
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'address': '/var/run/syslog' if sys.platform == 'darwin' else '/dev/log',
            'facility': SysLogHandler.LOG_LOCAL2,
            'formatter': 'verbose',
        }
    },
    'root': {
        'handlers': ['console', 'syslog'],
        'level': os.getenv('DJANGO_LOG_LEVEL', logging.INFO)
    }
}

logging.config.dictConfig(LOGGING)
