# -*- coding: utf-8 -*-
from django.conf import settings


def site_pages(request):

    context = {}
    context['DEPLOYMENT_MODE'] = settings.DEPLOYMENT_MODE
    context['SITE_NAME'] = settings.SITE_NAME
    context['SITE_ROOT_URI'] = settings.SITE_ROOT_URI
    # context['user_timezone'] = request.session.get('user_timezone')

    if hasattr(request, 'user'):
        context['user'] = request.user

    if hasattr(request, 'base_template') and request.base_template:
        context['BASE_TEMPLATE'] = request.base_template
    else:
        request.base_template = "base_standard.html"
        context['BASE_TEMPLATE'] = "base_standard.html"

    return context
