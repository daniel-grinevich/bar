from django.views.generic import CreateView, ListView, View, TemplateView
from .models import Order, OrderItem, Ticket
from .forms import OrderForm, OrderItemForm, OrderItemFormSet, TicketForm
from django.urls import reverse_lazy
from django.http import JsonResponse
import json
from recipe.models import MenuItem


# Create your views here.


class Dashboard(TemplateView):
    template_name = "order/dashboard.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the list of all menu items
        context["menu_items"] = MenuItem.objects.all()
        return context


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "order/order_create_form.html"
    success_url = reverse_lazy("order_list")

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     # Assuming 'menu_items' are the IDs of the items selected
    #     menu_items_ids = self.request.POST.getlist('menu_items')
    #     for item_id in menu_items_ids:
    #         menu_item = MenuItem.objects.get(id=item_id)
    #         OrderItem.objects.create(order=self.object, menu_item=menu_item, quantity=1)
    #     # Respond in a way suitable for HTMX (e.g., updating a part of the page)
    #     return JsonResponse({'status': 'success', 'order_id': self.object.id})


class OrderListView(ListView):
    model = Order
    template_name = "order/order_list.html"
    context_object_name = "orders"


class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = "order/orderitem_create_form.html"
    success_url = reverse_lazy("orderitem_list")


class OrderItemListView(ListView):
    model = OrderItem
    template_name = "order/orderitem_list.html"
    context_object_name = "orderitems"


class TicketCreateView(View):
    template_name = "tickets/create_ticket.html"

    def post(self, request, *args, **kwargs):

        if request.htmx:

            menu_items = request.POST.getlist("item_id")
            quantities = request.POST.getlist("quantity")

            formset_data = {
                "status": "placed",
                "orderitem_set-TOTAL_FORMS": str(len(menu_items)),
                "orderitem_set-INITIAL_FORMS": "0",
            }
            for i, (item_id, quantity) in enumerate(zip(menu_items, quantities)):
                formset_data.update(
                    {
                        f"orderitem_set-{i}-item": item_id,
                        f"orderitem_set-{i}-quantity": quantity,
                    }
                )
            order_item_formset = OrderItemFormSet(formset_data)
            ticket_form = TicketForm({"status": "placed"})
            new_ticket = ticket_form.save(commit=False)
            if order_item_formset.is_valid():
                new_ticket.save()
                instances = order_item_formset.save(commit=False)
                for instance in instances:
                    instance.ticket = new_ticket
                    instance.save()

        return JsonResponse({"status": "success"}, status=200)


# "equipment": self.equipment.id,
# "status": "placed",
# "orderitem_set-TOTAL_FORMS": "2",
# "orderitem_set-INITIAL_FORMS": "0",
# "orderitem_set-0-item": self.menu_item1.id,
# "orderitem_set-0-quantity": "2",
# "orderitem_set-1-item": self.menu_item2.id,
# "orderitem_set-1-quantity": "1",


# # class CreateTicketView(CreateView):
#     model = Ticket
#     form_class = TicketForm
#     template_name = "your_template_name.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.POST:
#             context["formset"] = OrderItemFormSet(self.request.POST)
#         else:
#             context["formset"] = OrderItemFormSet()
#         return context

#     def form_valid(self, form):
#         context = self.get_context_data()
#         formset = context["formset"]
#         if formset.is_valid():
#             self.object = form.save()
#             formset.instance = self.object
#             formset.save()
#             return JsonResponse(
#                 {"status": "success", "ticket_id": self.object.id}, status=200
#             )
#         else:
#             return self.form_invalid(form)

#     def form_invalid(self, form):
#         context = self.get_context_data()
#         return JsonResponse({"status": "error", "errors": form.errors}, status=400)
