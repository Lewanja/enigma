from django.urls import path
from . import views

urlpatterns = [
    path('book_session/', views.create_booking, name='book_session'),
]
