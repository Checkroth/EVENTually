from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.views',
    url(r'^my_events/$', 'my_events', name='my_events'),
)
