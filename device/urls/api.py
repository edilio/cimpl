from django.conf.urls import patterns, url

from rest_framework import routers

from ..views import api as views

router = routers.SimpleRouter()
router.register(r'locations', views.LocationViewSet)
router.register(r'device-types', views.DeviceTypeViewSet)
router.register(r'devices', views.DeviceViewSet)
router.register(r'parameters', views.ParameterViewSet)
router.register(r'values', views.ValueViewSet)

urlpatterns = router.urls

urlpatterns += patterns('device.views',

    # url(r'^aws-regions$', views.aws_regions, name='aws_regions'),

)

