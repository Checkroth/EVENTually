from django.conf.urls import patterns, include, url

urlpatterns = patterns('static_pages.views',
    url(r'^dashboard/$', 'dashboard', name='dashboard'),
    url(r'^$', 'about', name='about'),
)
