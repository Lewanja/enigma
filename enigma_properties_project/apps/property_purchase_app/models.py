from django.db import models

from enigma_properties_project.apps.properties_app.models import Property
from django.contrib.auth.models import User


class PurchaseProperty(models.Model):

    purchase_id = models.BigIntegerField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    property_price = models.IntegerField(default=2000000)