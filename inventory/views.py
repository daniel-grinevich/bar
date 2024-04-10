from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BarInventoryItemForm, BarInventoryProductForm, PurchaseItemFormSet
from .models import BarInventoryItem, BarInventoryProduct, Purchase, PurchaseItem
from django.views.generic import (
    View,
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    FormView,
)
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.urls import reverse


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

    def get_success_url(self):
        return reverse("inventory:purchases_item_edit", kwargs={"pk": self.object.pk})


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = "inventory/purchases_detail.html"


class PurchaseItemEditView(SingleObjectMixin, FormView):
    model = Purchase
    template_name = "inventory/purchase_item_edit.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Purchase.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Purchase.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return PurchaseItemFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Changes were saved")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("inventory:purchases_detail", kwargs={"pk": self.object.pk})
