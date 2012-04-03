from django.conf.urls.defaults import *
from django.conf import settings
from os import path as os_path

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from contact_form.views import contact_form
from scutils.forms import SCContactForm

from django.contrib import admin
admin.autodiscover()

from ct_groups.models import CTGroup
from ct_groups.feeds import BlogPostsPublicFeed 
from tagging.models import Tag
from wiki import views as wiki_views

try:
    email_login = settings.EMAIL_LOGIN
except AttributeError:
    email_login = True

urlpatterns = patterns('',
    # Example:
    url(r'^$', 'home.views.home', name='home'),
    url(r'^s/setlang/$', 'ct_groups.views.setlang', name='set-lang'),
    url(r'^process-digests/$', 'ct_groups.views.do_digests', name="process-digests"),

    (r'^templates/', include('ct_template.urls')),
    (r'^groups/', include('ct_groups.urls')),
    (r'^ct_groups/', include('ct_groups.urls')),
    url(r'^tags/$', ListView.as_view(
        queryset=Tag.objects.all(),
        paginate_by=400,
        template_name='topics/topic_list.html'), name="tags"),
    url(r'^tags/(?P<slug>[^/]+)/$', DetailView.as_view( 
        queryset=Tag.objects.all(), 
        slug_field='name',
        template_name='topics/topic_detail.html'), name="tag"),

    url(r'^accounts/profile/$', 'ct_groups.views.profile', name='profile'),
    (r'^accounts/profile/changed/$', TemplateView.as_view(template_name='registration/profile_changed.html')),

    (r'^blog/', include('ct_blog.urls')),
    (r'^comments/', include('django.contrib.comments.urls')) ,
    url(r'^contact/$', contact_form, { 'form_class': SCContactForm }, name='contact_form'),
    url(r'^contact/sent/$', TemplateView.as_view(template_name='contact_form/contact_form_sent.html'),
        name='contact_form_sent'),

    (r'^feeds/latestnews/$', BlogPostsPublicFeed()),
    (r'^notices/', include('notification.urls')),

    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^admin/', include(admin.site.urls)),
    (r'^r/', include('django.conf.urls.shortcut')),
)
if email_login:
    urlpatterns += patterns('ct_framework.views',
        url(r'^accounts/login/$', 'login', name='login'),
    )

urlpatterns += patterns('django.contrib.auth.views',
    (r'^password_reset/$','password_reset' ),
    (r'^password_reset/done/$', 'password_reset_done' ),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm'),
    (r'^reset/done/$', 'password_reset_complete'),
    (r'^accounts/password_change/$', 'password_change' ),
    (r'^accounts/password_change/done/$', 'password_change_done' ),
)

urlpatterns += patterns('',
    (r'^accounts/register/$', 'registration.views.register',
        {'backend': 'ct_framework.registration_backends.CTRegistrationBackend'}),
    (r'^accounts/', include('registration.backends.default.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os_path.join(settings.PROJECT_PATH, 'media')}),
    )
if settings.TESTING or settings.DEBUG:
    urlpatterns += patterns('',
       (r'', include('wiki.static_urls')), # static files, testing only
       (r'^fr/', include('ct_fileresource.urls')), # testing only
    )
