from django import forms
from enigma_properties_project.apps.property_interested_app.models import PropertyInterested


class BookingForm(forms.ModelForm):
    class Meta:
        model = PropertyInterested
        fields = ['interested_property_id']