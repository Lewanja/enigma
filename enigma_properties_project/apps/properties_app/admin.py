from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Property


# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ("available_property",
                    "property_id",
                    "property_name",
                    "property_description",
                    "property_location",
                    "available_property")
    list_filter = ("property_location",
                    "available_property")
    search_fields = ('property_name', 'property_location')

class MyAdminSite(AdminSite):
    site_header = 'Enigma Properties'
    site_title = 'Admin Portal'
    index_title = 'Welcome to Enigma Properties '

admin_site = MyAdminSite(name='myadmin')

admin.site.register(Property, PropertyAdmin)

