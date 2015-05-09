from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.views',
    url(r'^my_events/$', 'my_events', name='my_events'),
    url(r'^my_events_json/$', 'my_events_json', name='my_events_json'),
    url(r'^create_event/$', 'create_event', name='create_event'),
    url(r'^event/(?P<event_id>[0-9]+)/$', 'show_event', name='show_event'),
    url(r'^event/(?P<event_id>[0-9]+)/invite/$', 'invite', name='invite'),
    url(r'^event_inbox/$', 'event_inbox', name='event_inbox'),
    url(r'^event_inbox_json/$', 'event_inbox_json', name='event_inbox_json')
)
