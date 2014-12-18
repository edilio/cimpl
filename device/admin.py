from django.contrib import admin

from . models import Location, DeviceType, Device, Parameter, Value

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(DeviceType)
class DeviceType(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'device_type')
    search_fields = ('name', )
    list_filter = ('device_type', 'location',)


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_type', 'format', 'default_value')
    search_fields = ('name', )
    list_filter = ('device_type', )


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('device', 'parameter', 'value', 'applied')
    search_fields = ('name', )
    list_filter = ('applied', )