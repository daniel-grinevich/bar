# core/urls.py
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
