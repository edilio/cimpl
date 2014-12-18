from __future__ import unicode_literals

from django.conf.urls import patterns, url

urlpatterns = patterns('device.views.html',
    url(r'^$', 'home', name='home'),
)
