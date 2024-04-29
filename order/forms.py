from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "custom_user",
            "customer",
            "items",
            "total",
            "tip",
            "date_time",
            "reservation",
            "status",
        ]
