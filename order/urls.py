# core/urls.py
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path("order/create/", views.CreateOrder.as_view(), name="order_create"),
    path("orders/", views.OrderListView.as_view(), name="order_list"),
]
