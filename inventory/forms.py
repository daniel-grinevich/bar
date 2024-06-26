from django import forms
from .models import (
    BarInventoryItem,
    BarInventoryProduct,
    Purchase,
    PurchaseItem,
    Brand,
    ProductCategory,
)


class BarInventoryItemForm(forms.ModelForm):
    class Meta:
        model = BarInventoryItem
        fields = [
            "name",
            "level",
            "location",
            "date_expired",
            "product",
        ]
        widgets = {
            "date_expired": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }


BarInventoryItemFormSet = forms.modelformset_factory(
    BarInventoryItem, form=BarInventoryItemForm
)


class BarInventoryProductForm(forms.ModelForm):
    class Meta:
        model = BarInventoryProduct
        fields = [
            "name",
            "brand",
            "category",
            "size",
            "refridgerated",
            "par_level",
            "quantity",
            "location",
        ]


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = [
            "name",
            "date_purchased",
        ]
        widgets = {
            "date_purchased": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }


class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = [
            "purchase",
            "product",
            "quantity",
            "purchase_price",
            "location",
        ]


PurchaseItemFormSet = forms.inlineformset_factory(
    Purchase,
    PurchaseItem,
    fields=(
        "purchase",
        "product",
        "quantity",
        "purchase_price",
        "location",
    ),
    form=PurchaseItemForm,
    extra=3,
    min_num=1,
)


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            "name",
        ]


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = [
            "name",
        ]
