# -*- coding: utf-8 -*-
from .settings import INSTALLED_APPS
from .settings import MIDDLEWARE_CLASSES

DEBUG = True
DEPLOYMENT_MODE = 'local'
SITE_DOMAIN = '127.0.0.1'
# Port used when running locally
LOCAL_PORT = 8001

SITE_ROOT_URI = 'http://{0}:{1}/'.format(SITE_DOMAIN, LOCAL_PORT)
# For now, don't bother running locally over HTTPS
SITE_ROOT_URI_SECURE = 'https://{0}:{1}/'.format(SITE_DOMAIN, LOCAL_PORT)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mysite.server.wsgi.application'

PIPELINE_LESS_BINARY = '/usr/local/bin/lessc'

# When running locally just print emails to the console...
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_FROM_EMAIL = 'noreply@mysite.com'

# SESSION_COOKIE_DOMAIN = '.mysite.com'
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
CSRF_COOKIE_DOMAIN = '.mysite.com'

# By default, turn template caching off for local development so you can make
# template changes without having to restart the dev server.
# If you DO want template caching while running locally, simply copy
# TEMPLATE_LOADERS from settings.py to a my_settings.py
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

INTERNAL_IPS = ('127.0.0.1',)
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

from mysite.site_settings.local.database import *
from mysite.site_settings.local.social import *
from mysite.site_settings.local.logging import *
from mysite.site_settings.local.debug_toolbar import *

# Anyone on the team can create their own settings_mine.py if they'd like to
# override the standard local settings. This settings_mine.py is included
# in SVN ignore
try:
    from settings_mine import *
except ImportError:
    pass
