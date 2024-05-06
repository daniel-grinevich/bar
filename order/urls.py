# core/urls.py
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path("ordermenu/", views.OrderMenuTemplateView.as_view(), name="menu"),
    path("order/create/", views.OrderCreateView.as_view(), name="order_create"),
    path("orders/", views.OrderListView.as_view(), name="order_list"),
    path(
        "orderitem/create/",
        views.OrderItemCreateView.as_view(),
        name="orderitem_create",
    ),
    path("orderitems/", views.OrderItemListView.as_view(), name="orderitem_list"),
    path("ticket/create/", views.TicketCreateView.as_view(), name="ticket_create"),
    path("tickets/", views.TicketListView.as_view(), name="ticket_list"),
]
