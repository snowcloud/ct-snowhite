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
export DJANGO_SETTINGS_MODULE=snowhite.settings

./manage.py syncdb
./manage.py migrate --fake

./manage.py loaddata apps/home/fixtures/blog
./manage.py loaddata apps/home/fixtures/comments
./manage.py loaddata apps/home/fixtures/ct_groups
./manage.py loaddata apps/home/fixtures/ct_template
./manage.py loaddata apps/home/fixtures/flatpages
./manage.py loaddata apps/home/fixtures/sites
./manage.py loaddata apps/home/fixtures/users

cd static/css/
ln -s ../../../src/ct-template/ct_template/static/css/ct_template.css 
ln -s ../../../src/ct-template/ct_template/static/css/ct_template_enhanced.css
cd ../
ln -s ../../src/ct-template/ct_template/static/js
ln -s ../../src/ct-template/ct_template/static/images

