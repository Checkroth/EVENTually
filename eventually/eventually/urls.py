from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
urlpatterns = patterns('',
    (r'', include('accounts.urls')),
    (r'', include('events.urls')),
    (r'', include('static_pages.urls')),
    # (r'', include('subevents.urls')),

    (r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )