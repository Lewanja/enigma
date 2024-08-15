from django.forms import ModelForm
from enigma_properties_project.apps.properties_app.models import Property


class AddPropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = ['property_id','property_name', 'property_description', 'property_location',"available_property"]