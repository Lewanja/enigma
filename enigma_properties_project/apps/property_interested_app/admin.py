from django.contrib import admin
from .models import PropertyInterested

# Register your models here.
@admin.register(PropertyInterested)
class PropertyInterestedAdmin(admin.ModelAdmin):
    pass