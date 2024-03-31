from django import forms
from .models import BarInventoryItem, BarInventoryProduct, Purchase


class BarInventoryItemForm(forms.ModelForm):
    class Meta:
        model = BarInventoryItem
        fields = [
            "name",
            "level",
            "location",
        ]


class BarInventoryProductForm(forms.ModelForm):
    class Meta:
        model = BarInventoryProduct
        fields = [
            "name",
            "brand",
        ]


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = [
            "name",
        ]


PurchaseFormSet = forms.inlineformset_factory(
    Purchase,
    BarInventoryItem,
    fields=("__all__"),
    form=BarInventoryItemForm,
    extra=0,
    min_num=1,
)
