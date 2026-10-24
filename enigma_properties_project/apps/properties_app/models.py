from django.db import models

# Create your models here.
class Property(models.Model):
    property_status = {
        "Available": "available",
        "Sold": "sold",
    }
    property_id = models.BigIntegerField(primary_key=True)
    property_name = models.CharField(max_length=200)
    property_description = models.CharField(max_length=250)
    property_location = models.CharField(max_length=250)
    available_property = models.CharField(max_length=20, choices=property_status, default="Available")


    def __str__(self):
        return self.property_name