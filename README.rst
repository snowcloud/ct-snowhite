Snowhite
============
:Info: See `the ClinicalTemplates.org web site <http://clinicaltemplates.org>`_ for more information. 
:Author: Derek Hoy <derek@snowcloud.co.uk>

About
-----
This is a starter `Django <http://djangoproject.com>`_ project for the ClinicalTemplates web framework.

*Please note- this is incomplete and not currently installable.*

git clone into directory
cd directory
pip install -r requirements.txt

Note here about adding links in /static/ to ct_template css, js.

Initializing database
-----
cd ct-snowhite/snowhite

./manage.py syncdb
./manage.py migrate --fake

chmod +x post_install
./post_install

