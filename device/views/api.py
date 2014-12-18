from rest_framework import generics, filters, viewsets, mixins, status, serializers

from ..serializers import *
from ..models import *


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    model = Location


class DeviceTypeViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceTypeSerializer
    model = DeviceType


class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    model = Device


class ParameterViewSet(viewsets.ModelViewSet):
    serializer_class = ParameterSerializer
    model = Parameter


class ValueViewSet(viewsets.ModelViewSet):
    serializer_class = ValueSerializer
    model = Value
