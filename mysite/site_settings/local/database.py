from mysite.site_settings.settings import here

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': here('mysite.sqlite'),
    }
}
