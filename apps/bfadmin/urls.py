from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()


# The main site
urlpatterns = patterns(
    'bfadmin.views',
    url(r'^$', 'welcome'),
)


# Imported sites
urlpatterns += patterns(
    '',
    url(r'^api/calendar/', include('gcalendar.urls')),
    url(r'^account/', include('profile.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += staticfiles_urlpatterns()
