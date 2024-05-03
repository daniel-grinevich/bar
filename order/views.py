from django.views.generic import CreateView, ListView
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemForm
from django.urls import reverse_lazy

# Create your views here.


class CreateOrder(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "order/order_create_form.html"
    success_url = reverse_lazy("order_list")


class OrderListView(ListView):
    model = Order
    template_name = "order/order_list.html"
    context_object_name = "orders"


class CreateOrderItem(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = "order/orderitem_create_form.html"
    success_url = reverse_lazy("orderitem_list")


class OrderItemListView(ListView):
    model = OrderItem
    template_name = "order/orderitem_list.html"
    context_object_name = "orderitems"
