from . import views
from.views import AddProperty
from django.urls import path

urlpatterns = [
    path('list_property',views.list_properties, name="list_property"),
    path('view_property/<int:property_id>/',views.view_properties, name="view_property"),
    path('about', views.about, name="about"),
    path('add_property', AddProperty.as_view(), name="add_property"),
]