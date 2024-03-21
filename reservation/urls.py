# core/urls.py
from django.urls import path
from . import views

app_name = "reservation"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("detail/<int:pk>/", views.detail, name="detail"),  # Updated path
    path("create/", views.create, name="create"),
]
