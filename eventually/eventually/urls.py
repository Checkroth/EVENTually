from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # (r'', include('accounts.urls')),
    (r'', include('events.urls')),
    # (r'', include('subevents.urls')),

    (r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
