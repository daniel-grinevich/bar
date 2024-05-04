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
        fields = ["equipment", "status"]


# PurchaseItemFormSet = forms.inlineformset_factory(
#     Purchase,
#     PurchaseItem,
#     fields=(
#         "purchase",
#         "product",
#         "quantity",
#         "purchase_price",
#         "location",
#     ),
#     form=PurchaseItemForm,
#     extra=3,
#     min_num=1,
# )

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
            "reservation",
            "status",
        ]
