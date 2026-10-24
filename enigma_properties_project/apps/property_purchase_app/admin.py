from django.contrib import admin
from .models import PurchaseProperty


# Register your models here.
@admin.register(PurchaseProperty)
class PurchasePropertyAdmin(admin.ModelAdmin):
    pass
