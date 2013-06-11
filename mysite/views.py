# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


class HomeView(TemplateView):
    template_name = 'index.html'


class FAQView(TemplateView):
    template_name = 'faq.html'


class TermsView(TemplateView):
    template_name = 'terms.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'privacy.html'


class LoginView(FormView):
    template_name = 'login.html'


class LogoutView(FormView):
    template_name = 'logout.html'
