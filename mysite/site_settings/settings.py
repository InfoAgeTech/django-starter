# -*- coding: utf-8 -*-
import os
import sys
import manage

# Do not run in DEBUG in production!!!
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# The site name that appears throughout the site.
SITE_NAME = unicode('My Site Name')

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

STATIC_ROOT = os.path.join(SITE_ROOT, '../collected_static')
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Ensure Django templates are cached in "real" deployments. This can be
# overridden locally so template changes are reflected immediately.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
     'django.template.loaders.filesystem.Loader',
     'django.template.loaders.app_directories.Loader',
    )),
)

# Django Messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    # 'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    # 'social_auth.backends.google.GoogleBackend',
    # 'social_auth.backends.yahoo.YahooBackend',
    # 'social_auth.backends.OpenIDBackend',
)

ROOT_URLCONF = 'mysite.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite',
    'pipeline',
    'social_auth',
)

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates')
)

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
STATIC_URL = '/static/'
MEDIA_URL = ''

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'mysite.custom_context_processors.site_pages',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',

    # Social auth dependencies
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

# Define if you're using a different user model.
# AUTH_USER_MODEL = 'my_app_name.User'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
# Uncomment if using a custom user model
# SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
)

# Specific extra social auth permissions needed.
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
GOOGLE_OAUTH2_EXTENDED_PERMISSIONS = ['email']
# This doesn't work because twitter doesn't give an email address
TWITTER_EXTENDED_PERMISSIONS = ['email']

# # Session related settings.
# # See: http://docs.djangoproject.com/en/dev/topics/http/sessions/#settings
SESSION_COOKIE_NAME = 'mysite'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_ENGINE = 'mongoengine.django.sessions'
SESSION_COOKIE_AGE = 60 * 60 * 12  # Session cookie for 12 hours

# Added in django 1.5 secret key is required.  This is a random generated string.
# Change this to some unique string.
SECRET_KEY = '123456789abcdefg'

# Added in django 1.4.4. See: https://docs.djangoproject.com/en/1.4/releases/1.4.4/#host-header-poisoning
ALLOWED_HOSTS = ['*']

from .settings_pipeline import *

try:
    from .settings_deployment import *
except ImportError:
    from .settings_local import *

if 'test' in sys.argv:
    # Run tests in memory
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    INSTALLED_APPS += ('django_nose',)
    NOSE_ARGS = ('--cover-package=mysite', '--nocapture',
                 '--with-doctest', '--testmatch=^test')
