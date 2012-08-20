from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'views',
    url(r'^$', 'display'),
    url(r'^admin/', 'admin')
)
