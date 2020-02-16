from django.urls import path, include
from .views import *

app_name = "favourite"
urlpatterns = [
    path('list-create', FavouriteListCreateAPIView.as_view(), name="list-create"),
    path('update-delete/<pk>', FavouriteAPIView.as_view(), name="update-delete"),
    path('all/<pk>', FavouriteAllAPIView.as_view(), name="all"),
]
