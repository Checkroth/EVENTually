from django.conf.urls import patterns, include, url

urlpatterns = patterns('subevents.views',
    url(r'^(?P<event_id>[0-9]+)/create_subevent/$', 'create_subevent', name='create_subevent'),
    url(r'^event/(?P<event_id>[0-9]+)/(?P<subevent_id>[0-9]+)/$', 'show_subevent', name='show_subevent')
)
