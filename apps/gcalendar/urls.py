from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'gcalendar.views',
    url(r'^(?P<slug>\w+)/?(?P<html>(html)?)$', 'embed_calendar_html'),
)
