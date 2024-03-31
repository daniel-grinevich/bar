from django.shortcuts import render
from .forms import BarInventoryItemForm, BarInventoryProductForm
from .models import BarInventoryItem, BarInventoryProduct, Purchase
from django.views.generic import View, CreateView, UpdateView, ListView, DetailView
from django.contrib import messages


# Create your views here.


class CreateInventoryItem(CreateView):
    model = BarInventoryItem
    form_class = BarInventoryItemForm
    template_name_suffix = "_create_form"


class CreateBarInventoryProduct(CreateView):
    model = BarInventoryProduct
    form_class = BarInventoryProductForm
    template_name_suffix = "_create_form"


class PurchaseListView(ListView):
    model = Purchase
    template_name = "inventory/purchases.html"


class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = "inventory/purchases_create.html"
    fields = ["name"]

    def form_valid(self, form):

        messages.add_message(self.request, messages.SUCCESS, "Purchase Created")

        return super().form_valid(form)


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = "inventory/purchases_detail.html"
