from django.urls import path, include
from .views import *

app_name = "account"
urlpatterns = [
    path('me', ProfileView.as_view(), name="me"),
    path('change-password', UpdatePassword.as_view(), name="change-password"),
    path('register', CreateUserView.as_view(), name="register"),
]
