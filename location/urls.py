from django.urls import path
from . import views

app_name = "location"

urlpatterns = [
    # Generic URLs
    path("dashboard/", views.Dashboard.as_view(), name="dashboard"),
    # Location URLs
    path(
        "locations/create/", views.LocationCreateView.as_view(), name="location_create"
    ),
    path("locations/", views.LocationListView.as_view(), name="location_list"),
    path(
        "locations/<int:pk>/",
        views.LocationDetailView.as_view(),
        name="location_detail",
    ),
    path(
        "locations/<int:pk>/update/",
        views.LocationUpdateView.as_view(),
        name="location_update",
    ),
    path(
        "locations/<int:pk>/delete/",
        views.LocationDeleteView.as_view(),
        name="location_delete",
    ),
    # Table URLs
    path("tables/create/", views.TableCreateView.as_view(), name="table_create"),
    path("tables/", views.TableListView.as_view(), name="table_list"),
    path("tables/<int:pk>/", views.TableDetailView.as_view(), name="table_detail"),
    path(
        "tables/<int:pk>/update/", views.TableUpdateView.as_view(), name="table_update"
    ),
    path(
        "tables/<int:pk>/delete/", views.TableDeleteView.as_view(), name="table_delete"
    ),
]
