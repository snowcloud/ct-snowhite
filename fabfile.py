from __future__ import with_statement
from fabric.api import *
    
def up_reqs(upgrade=False):
    """docstring for up_reqs: fab up_reqs:upgrade """
    upgrade = '--upgrade' if upgrade == 'upgrade' else ''
    local('pip install -r requirements.txt')
    
def pull_codebase():
    print("updating code...")
    # local('cd ~/virtualenvs/icnp && git pull')
    local('pip install -r requirements.txt --upgrade')

def use_head():
	proj='snowhite'
    local('cd ~/virtualenvs/%s && git checkout master' % proj)
    local('cd ~/virtualenvs/%s/src/ct-blog && git checkout master' % proj)
    local('cd ~/virtualenvs/%s/src/ct-framework && git checkout master' % proj)
    local('cd ~/virtualenvs/%s/src/ct-groups && git checkout master' % proj)
    local('cd ~/virtualenvs/%s/src/ct-template && git checkout master' % proj)
    local('cd ~/virtualenvs/%s/src/ct-wikiapp && git checkout master' % proj)
    local('cd ~/virtualenvs/%s/src/sc-utils && git checkout master' % proj)

def use_dev():
	proj='snowhite'
    warn("NEEDS A git checkout -b newone origin/newone IN EACH APP BEFORE FIRST TIME")
    local('cd ~/virtualenvs/%s && git checkout restyle-newlook' % proj)
    local('cd ~/virtualenvs/%s/src/ct-blog && git checkout master' % proj)
    local('cd ~/virtualenvs/%s/src/ct-framework && git checkout restyle' % proj)
    local('cd ~/virtualenvs/%s/src/ct-groups && git checkout restyle' % proj)
    local('cd ~/virtualenvs/%s/src/ct-template && git checkout dev' % proj)
    local('cd ~/virtualenvs/%s/src/ct-wikiapp && git checkout master' % proj)
    local('cd ~/virtualenvs/%s/src/sc-utils && git checkout master' % proj)

"""
cd ~/virtualenvs/snowhite/src/ct-framework
git checkout -b dev origin/dev
cd ~/virtualenvs/snowhite/src/ct-groups
git checkout -b dev origin/dev
cd ~/virtualenvs/snowhite/src/ct-template
git checkout -b newone origin/newone
"""
	
