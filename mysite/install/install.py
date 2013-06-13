#!/usr/bin/env python
# encoding: utf-8
"""
Creates a new instance of a django site based on the django-starter project at:

https://github.com/InfoAgeTech/django-starter
"""
import shlex
import subprocess
import os
from optparse import OptionParser

import pip


def main():
    """ 
    TODO
    ====
    
    - clone starter project
    - remove git history (remove all .git folders)
    - accept name as param option for what to name project
    - initialize as new git project
    - provide name for virtual environment
        - if name exists go to it
        - if doesn't exist, create new virtual environment
    - install dependencies
    - commit new site to remote repo.
    
    See: http://stackoverflow.com/questions/12842455/create-new-clean-repository-from-a-clone-of-a-remote-repository-get-rid-of-hist
    """
    pass

if __name__ == '__main__':
    main()

