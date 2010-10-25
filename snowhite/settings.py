# coding=UTF-8
# Django settings for snowhite project.

import os
import sys

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('your name', 'email@exmaple.com'),
)

CONTACT_EMAILS = MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'snowhitedb',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/London'
DATE_FORMAT='%d %B %Y, %H:%M'
SITE_ID = 1
USE_I18N = True
LANGUAGE_CODE = 'en-gb'

ugettext = lambda s: s
LANGUAGES = (
    ('nl', ugettext('Dutch')),
    ('en', ugettext('English')),
)

PROJECT_PATH = os.path.abspath(os.path.split(__file__)[0])

sys.path.insert(0, os.path.join(PROJECT_PATH, "apps"))
# sys.path.insert(0, os.path.join(PROJECT_PATH, "libs"))
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'static')
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'sitetemplates')
)

ADMIN_MEDIA_PREFIX = '/admin/media/'
# this doesn't need to be secure...
SECRET_KEY = 'W03uCcybKXMWUShFRariiEBgEozLaQOLrfkiGZpsRZAtOYvuMv'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    # "shared_apps.shared_utils.views.set_vars", 
)

# NB applied in order, except response/process middleware applied in reverse !!!
MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    # "django.contrib.csrf.middleware.CsrfResponseMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.doc.XViewMiddleware",
    # "pagination.middleware.PaginationMiddleware",
    # "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    # "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    # "shared_utils.middleware.Custom403Middleware"
)
ROOT_URLCONF = 'snowhite.urls'

INSTALLED_APPS = (
    # 'ct_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.comments',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    # 'django_openid_auth',
    #     'home',
    #     'ct_groups',
    #     'ct_template',
    #     'basic.blog',
    #     'basic.inlines',
    #     'contact_form',
    #     'notification',
    #     'photologue',
    #     'registration',
    #     'renderform',
    # 'south',
    #     'tagging',
    #     'wiki',
    #     'pagination',
    #     'timezones',
    #     'scutils',

)

ACCOUNT_ACTIVATION_DAYS = 10 # days

# django-wikiapp settings
STATIC_MEDIA_PATH = MEDIA_ROOT
WIKI_REQUIRES_LOGIN=False
WIKI_URL_RE='[^/]+'

# override any of the above in your own settings_local.py
try:
    from settings_local import *
except ImportError:
    pass

