from django import forms
from .models import Order, OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
            "order",
            "item",
            "quantity",
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "custom_user",
            "customer",
            "total",
            "tip",
            "date_time",
            "reservation",
            "status",
        ]
