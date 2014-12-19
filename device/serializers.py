from rest_framework import serializers

from models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType


class DeviceSerializer(serializers.ModelSerializer):
    location_str = serializers.CharField(source='location.name', read_only=True)

    class Meta:
        model = Device


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value