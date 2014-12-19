from __future__ import unicode_literals

from django.conf.urls import patterns, url

urlpatterns = patterns('device.views.html',
    url(r'^devices$', 'devices', name='devices'),
    url(r'^account$', 'account', name='account'),
    url(r'^test-angular$', 'angular', name='angular'),
    url(r'^$', 'home', name='home'),

)

