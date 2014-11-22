from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.views',
    url(r'^my_events/$', 'my_events', name='my_events'),
    url(r'^create_event/$', 'create_event', name='create_event'),
    url(r'^event/(?P<event_id>[0-9]+)/$', 'show_event', name='show_event')
)
