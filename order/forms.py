from django import forms
from .models import Order, OrderItem, Ticket
from django.forms import inlineformset_factory


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
            "ticket",
            "item",
            "quantity",
        ]


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["equipment", "status", "reservation"]


OrderItemFormSet = inlineformset_factory(
    Ticket,
    OrderItem,
    form=OrderItemForm,
    extra=1,
    can_delete=True,
)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "custom_user",
            "customer",
            "total",
            "tip",
            "date_time",
            "status",
        ]
