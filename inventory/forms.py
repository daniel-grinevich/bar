from django import forms
from .models import (
    BarInventoryItem,
    BarInventoryProduct,
    Purchase,
    PurchaseItem,
    Brands,
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
        ]


class PurchaseItemForm(forms.ModelForm):

    class Meta:
        model = PurchaseItem
        fields = ["product", "date_purchased", "purchase_price", "purchase"]
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


PurchaseItemFormSet = forms.inlineformset_factory(
    Purchase,
    PurchaseItem,
    fields=("__all__"),
    form=PurchaseItemForm,
    extra=3,
    min_num=1,
)


class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = [
            "name",
        ]


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = [
            "name",
        ]
