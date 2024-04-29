from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Order
from .forms import OrderForm
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
