from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path("", views.CreateInventoryItem.as_view(), name="barinventoryitem_create_form"),
    path("purchases/", views.PurchaseListView.as_view(), name="purchases"),
    path("purchases/add/", views.PurchaseCreateView.as_view(), name="purchases_create"),
    path(
        "purchases/<int:pk>/",
        views.PurchaseDetailView.as_view(),
        name="purchases_detail",
    ),
]
