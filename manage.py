#!/usr/bin/env python
import os
import sys

managepy_location = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings.base'

if __name__ == "__main__":

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
