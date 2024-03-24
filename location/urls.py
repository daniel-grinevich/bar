# core/urls.py
from django.urls import path
from . import views

app_name = "location"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("create/location/", views.CreateLocation.as_view(), name="create_location"),
    path("create/table/", views.CreateTable.as_view(), name="create_table"),
]
