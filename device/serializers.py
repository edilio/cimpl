from rest_framework import serializers

from models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value