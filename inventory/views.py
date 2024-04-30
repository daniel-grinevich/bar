from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import (
    BarInventoryItemForm,
    BarInventoryProductForm,
    PurchaseItemFormSet,
    BrandForm,
    ProductCategoryForm,
    PurchaseForm,
)
from .models import (
    BarInventoryItem,
    BarInventoryProduct,
    Purchase,
    PurchaseItem,
    Brand,
    ProductCategory,
)
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
from django.db import transaction, IntegrityError

# Inventory Items


class BarInventoryItemCreateView(CreateView):
    model = BarInventoryItem
    form_class = BarInventoryItemForm
    template_name = "inventory/item/bar_inventory_item_form.html"

    def get_success_url(self):
        return reverse("inventory:inventory_items")


class BarInventoryItemListView(ListView):
    model = BarInventoryItem
    template_name = "inventory/item/bar_inventory_items.html"


# Inventory Products


class BarInventoryProductCreateView(CreateView):
    model = BarInventoryProduct
    form_class = BarInventoryProductForm
    template_name = "inventory/product/bar_inventory_product_form.html"

    def get_success_url(self):
        return reverse("inventory:inventory_products")


class BarInventoryProductListView(ListView):
    model = BarInventoryProduct
    template_name = "inventory/product/bar_inventory_products.html"


# Purchases
class PurchaseListView(ListView):
    model = Purchase
    template_name = "inventory/purchase/purchases.html"


class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = "inventory/purchase/purchase_form.html"
    form_class = PurchaseForm

    def form_valid(self, form):

        messages.add_message(self.request, messages.SUCCESS, "Purchase Created")

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("inventory:purchases_item_edit", kwargs={"pk": self.object.pk})


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = "inventory/purchase/purchases_detail.html"


def deliverPurchase(request, pk):
    purchase = Purchase.objects.get(pk=pk)
    purchase.delivered = True
    purchase.save()
    return HttpResponseRedirect(reverse("inventory:purchases"))


class PurchaseItemEditView(SingleObjectMixin, FormView):
    model = Purchase
    template_name = "inventory/purchase/item/purchase_item_edit.html"

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


# Brands
class BrandsListView(ListView):
    model = Brand
    template_name = "inventory/brand/brands.html"


class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = "inventory/brand/brand_form.html"

    def get_success_url(self):
        return reverse("inventory:brands")


# Product Categories
class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = "inventory/category/product_categories.html"


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = "inventory/category/product_category_form.html"

    def get_success_url(self):
        return reverse("inventory:categories")
