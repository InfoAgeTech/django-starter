# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin
from mysite.views import FAQView
from mysite.views import HomeView
from mysite.views import LoginView
from mysite.views import LogoutView
from mysite.views import PrivacyPolicyView
from mysite.views import TermsView

admin.autodiscover()


# TODO: Create class based views for these.
# handler403 = 'mysite.views.permission_denied_403'
# handler404 = 'mysite.views.page_not_found_404'
# handler500 = 'mysite.views.server_error_500'


urlpatterns = patterns('',
    url(r'^/?$', HomeView.as_view(), name='home'),
    url(r'^login/?$', LoginView.as_view(), name='login'),
    url(r'^logout/?$', LogoutView.as_view(), name='logout'),

    url(r'', include('social_auth.urls')),  # see: https://github.com/omab/django-social-auth/blob/master/social_auth/urls.py
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^faq/?$', FAQView.as_view(), name='faq'),
    url(r'^terms/?$', TermsView.as_view(), name='terms'),
    url(r'^privacy/?$', PrivacyPolicyView.as_view(), name='privacy'),
)

# When running locally, serve up static content via the django development
# server. Obviously not a cool thing to do in a "real" deployment.
if settings.DEPLOYMENT_MODE == 'local':
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
