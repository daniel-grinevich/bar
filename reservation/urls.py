# core/urls.py
from django.urls import path
from . import views

app_name = "reservation"

urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    # path("detail/<int:pk>/", views.detail, name="detail"),  # Updated path
    path(
        "reservation/create",
        views.CreateReservation.as_view(),
        name="reservation_create",
    ),
    path("event/create", views.CreateEvent.as_view(), name="event_create"),
]
