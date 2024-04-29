from django.urls import path
from .views import (
    DashboardView,
    CreateReservation,
    UpdateReservation,
    ReservationListView,
    ReservationDetailView,
    DeleteReservation,
    CreateEvent,
    UpdateEvent,
    EventListView,
    EventDetailView,
    DeleteEvent,
)

app_name = "reservation"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("reservations/", ReservationListView.as_view(), name="reservation_list"),
    path(
        "reservations/create/", CreateReservation.as_view(), name="reservation_create"
    ),
    path(
        "reservations/<int:pk>/",
        ReservationDetailView.as_view(),
        name="reservation_detail",
    ),
    path(
        "reservations/<int:pk>/update/",
        UpdateReservation.as_view(),
        name="reservation_update",
    ),
    path(
        "reservations/<int:pk>/delete/",
        DeleteReservation.as_view(),
        name="reservation_delete",
    ),
    path("events/", EventListView.as_view(), name="event_list"),
    path("events/create/", CreateEvent.as_view(), name="event_create"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("events/<int:pk>/update/", UpdateEvent.as_view(), name="event_update"),
    path("events/<int:pk>/delete/", DeleteEvent.as_view(), name="event_delete"),
]
