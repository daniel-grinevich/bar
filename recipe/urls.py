from django.urls import path
from . import views

app_name = "recipe"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("details/<int:pk>/", views.detail, name="detail"),
]
