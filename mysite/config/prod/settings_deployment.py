# -*- coding: utf-8 -*-

DEBUG = False
DEPLOYMENT_MODE = 'prod'

from mysite.site_settings.prod.database import *
from mysite.site_settings.prod.logging import *
from mysite.site_settings.prod.social import *
