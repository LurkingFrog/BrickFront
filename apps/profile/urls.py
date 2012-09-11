from django.conf.urls import patterns, url

urlpatterns = patterns(
    'profile.views',
    url(r'^login/$', 'user_login'),
    url(r'^logout/$', 'user_logout'),
)
