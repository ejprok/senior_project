from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0g!--#s7^298534i^&+azgqgmyb7xxn*+j6ds^_j%8u=s+888v'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS+[
    'debug_toolbar', # debug toolbar
]

MIDDLEWARE =  MIDDLEWARE+[
        'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERAL_IPS = ("127.0.0.1" , "127.17.0.1", "50.116.12.68:3001")

try:
    from .local import *
except ImportError:
    pass
