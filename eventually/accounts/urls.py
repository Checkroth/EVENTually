from django.conf.urls import patterns, include, url

urlpatterns = patterns('accounts.views',
    url(r'^accounts/signup/$', 'create_account', name='create_account'),
    url(r'^accounts/profile/$', 'profile', name='profile'),
    url(r'^accounts/confirmation/$', 'confirmation', name='confirmation'),
    url(r'^accounts/login/$', 'login', name='login'),
)
