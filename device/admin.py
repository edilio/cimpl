from django.contrib import admin

from . models import Location, DeviceType, Device

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



