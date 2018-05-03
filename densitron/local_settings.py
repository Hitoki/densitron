import sys

__author__ = 'vetal'

from .settings import *


INSTALLED_APPS += ('debug_toolbar', )

MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

DEBUG = True
TESTING = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'kidomakai@gmail.com'
EMAIL_HOST_PASSWORD = 'hitoki666'
