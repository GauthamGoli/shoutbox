from django.conf.urls import patterns, include, url
from django.contrib import admin
from shoutbox import urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forum_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^shoutbox/',include('shoutbox.urls')),
    url(r'^shoutbox/submit/',include('shoutbox.urls')),
)
