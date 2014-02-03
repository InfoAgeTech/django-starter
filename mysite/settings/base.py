from __future__ import unicode_literals

import os
import sys

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
SITE_NAME = 'My Site Name'

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
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    # TODO: when upgrading to django 1.6, see:
    # http://psa.matiasaguirre.net/docs/configuration/django.html#django-1-6
    # 'social.apps.django_app.utils.BackendWrapper',
    # 'social.backends.google.GoogleOpenId',
    # 'social.backends.google.GoogleOAuth',
    # 'social.backends.yahoo.YahooOpenId',
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
    'social.apps.django_app.default',
)

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates')
)

LOGIN_URL = '/login'
LOGIN_ERROR_URL = LOGIN_URL
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

# Used for python-social-auth
SOCIAL_AUTH_DEFAULT_USERNAME = 'social_'
SOCIAL_AUTH_UUID_LENGTH = 22
SOCIAL_AUTH_SLUGIFY_USERNAMES = True
SOCIAL_AUTH_CLEAN_USERNAMES = True
# Uncomment if using a custom user model
# SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
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

# Change this to some unique string.
SECRET_KEY = '123456789abcdefg'

ALLOWED_HOSTS = ['*']

from .settings_pipeline import *

try:
    from .settings_deployment import *
except ImportError:
    from .local.base import *

if 'test' in sys.argv:
    # Run tests in memory
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    INSTALLED_APPS += ('django_nose',)
    NOSE_ARGS = ('--cover-package=mysite', '--nocapture',
                 '--with-doctest', '--testmatch=^test')
