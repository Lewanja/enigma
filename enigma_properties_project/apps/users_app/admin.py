from django.contrib import admin
from .models import NewUser

# Register your models here.
@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    pass