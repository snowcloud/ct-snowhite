Snowhite
============
:Info: See `the project home page <http://snowcloud.github.com/ct-snowhite/>`_ for more information. 
:Author: Derek Hoy <derek@snowcloud.co.uk>

About
-----
This is a starter `Django <http://djangoproject.com>`_ project for the ClinicalTemplates web framework.

Installation
------------

It is recommended you install this into a working Django setup using `Virtualenv <http://pypi.python.org/pypi/virtualenv>`_- you can then clone the project with Git and do a `pip <http://www.pip-installer.org/>`_ install::

    git clone git://github.com/snowcloud/ct-snowhite
    
    # optional use of virtualenv
    virtualenv ct-snowhite
    source ct-snowhite/bin/activate
    
    cd ct-snowhite
    pip install -r requirements.txt
    
Setup database::

    cd ct-snowhite/snowhite
    ./manage.py syncdb
    ./manage.py migrate --fake

Install some default data fixtures::

    cd ct-snowhite
    chmod +x post_install
    post_install
    
Run the Django server::

    cd ct-snowhite/snowhite
    ./manage.py runserver 8080

View the project home page: http://127.0.0.1:8080
If you have run the post_install, you can now log in as ``admin/admin`` for full access. If you don't want to run post_install, use ``./manage.py createsuperuser``

