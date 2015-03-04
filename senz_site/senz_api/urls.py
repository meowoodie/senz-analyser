__author__ = 'woodie'

from django.conf.urls import patterns, include, url
from views import Senz

urlpatterns = patterns('senz_api.views',
    # Examples:
    # url(r'^$', 'senz_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^senz/$', Senz)
)
