from django.conf.urls import patterns, include, url
from django.contrib import admin
from senz_api import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'senz_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^senz/', include(urls))
)
