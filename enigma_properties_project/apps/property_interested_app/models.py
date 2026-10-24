
from django.db import models
from enigma_properties_project.apps.properties_app.models import Property
from django.contrib.auth.models import User


class PropertyInterested(models.Model):
    interested_property_id = models.ForeignKey(
        Property,
        on_delete=models.CASCADE)
    interested_user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE)




