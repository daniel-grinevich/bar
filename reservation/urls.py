# core/urls.py
from django.urls import path
from . import views

app_name = "reservation"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    # path("detail/<int:pk>/", views.detail, name="detail"),  # Updated path
    path(
        "create/reservation",
        views.CreateReservation.as_view(),
        name="create_reservation",
    ),
]
