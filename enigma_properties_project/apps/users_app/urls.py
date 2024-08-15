from django.urls import path
from . import views


urlpatterns =[path("login/",views.login_view,name="user_login"),
              path('register/', views.register_user, name='register'),]
