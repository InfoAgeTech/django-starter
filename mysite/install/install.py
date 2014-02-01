#!/usr/bin/env python
# encoding: utf-8
"""
Creates a new instance of a django site based on the django-starter project at:

https://github.com/infoagetech/django-starter
"""
import shlex
import subprocess
import os
from optparse import OptionParser

import pip


def main():
    """Project initializer to start a new project from scratch based on the 
    django-starter project:
    
    https://github.com/infoagetech/django-starter
    
    TODO
    ====
    
    Params
    ======
    -n    name of the project to create
    -l    location of the project.  This should be the absolute file path
    -v    virtual environment name.  If the virtual env exists, the new project
          will be added to the virtual environment.  If the virtual env doesn't
          exist, it will be created.
    
    See: 
    http://stackoverflow.com/questions/12842455/create-new-clean-repository-from-a-clone-of-a-remote-repository-get-rid-of-hist
    https://gist.github.com/robwierzbowski/5430952
    http://stackoverflow.com/questions/2423777/is-it-possible-to-create-a-remote-repo-on-github-from-the-cli-without-ssh
    """
    # clone starter project
    # git clone git@github.com:InfoAgeTech/django-starter.git my-project-name

    # remove git history (remove all .git folders)
    # cd my-project-name
    # rm -rf ./.git

    # initialize as new git project
    # git init

    # check to see if the provided virtual environment exists.  If not, create it.
    # get list of current virtual environments
    # lsvirtualenv
    # if name exists go to it
    #   workon virtual-env-name

    # if doesn't exist, create new virtual environment
    #   mkvirtualenv virtual-env-name

    # install dependencies
    # pip install -r requirements.txt

    # commit new site to remote repo.
    # TODO: do I want to do this?  Or just let the user add it?
    #       Or create the remote repo, but wait to push the code?

    pass

if __name__ == '__main__':
    main()

