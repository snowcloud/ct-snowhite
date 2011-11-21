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
