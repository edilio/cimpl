from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class DeviceType(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=50)
    device_type = models.ForeignKey(DeviceType)
    location = models.ForeignKey(Location)
    last_connection = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Parameter(models.Model):
    name = models.CharField(max_length=50)
    device_type = models.ForeignKey(DeviceType)
    format = models.CharField(max_length=100)
    default_value = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Value(models.Model):
    device = models.ForeignKey(Device)
    value = models.CharField(max_length=50)
    applied = models.BooleanField(default=False)

    def __unicode__(self):
        return self.device.name + ' --> ' + self.value