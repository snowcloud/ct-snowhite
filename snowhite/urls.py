from django.conf.urls.defaults import *
from django.conf import settings
from os import path as os_path


try:
    email_login = settings.EMAIL_LOGIN
except AttributeError:
    email_login = True


urlpatterns = patterns('',
    url(r'^$', 'home.views.home', name='home'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(.*)$', 'django.views.static.serve', {'document_root': os_path.join(settings.PROJECT_PATH, 'static')}),
    )
    # urlpatterns += patterns('',
    #    (r'', include('wiki.static_urls')), # static files, testing only
    # )
