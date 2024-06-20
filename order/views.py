from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, View, TemplateView
from .models import Order, OrderItem, Ticket
from .forms import OrderForm, OrderItemForm, OrderItemFormSet, TicketForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from recipe.models import MenuItem, Category, Option, Menu
from .mixins import JsonDeserializerMixin
import json

# Create your views here.


class OrderMenuTemplateView(TemplateView):
    template_name = "order/order_menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.prefetch_related("menu_items").all()
        context["menus"] = Menu.objects.all()
        return context


def get_menu_item_options(request):
    if request.htmx.request.method == "GET":
        item_id = request.GET.get("item_id")
        item_uuid = request.GET.get("item_uuid")
        menu_id = request.GET.get("menu_id")

        # Fetch the item name, assuming that 'name' is an attribute of MenuItem
        item = MenuItem.objects.get(id=item_id)

        # Fetch options and use select_related to optimize database access
        options_queryset = item.get_options()

        # Group options by classification
        classification_options = {}
        for option in options_queryset:
            if option.classification not in classification_options:
                classification_options[option.classification] = []
            classification_options[option.classification].append(option)

        context = {
            "classified_options": classification_options,
            "item_id": item_id,
            "item_name": item.name,
            "item_uuid": item_uuid,
            "menu_id": menu_id,
        }
        return render(request, "order/options_menu_partial.html", context)

    return JsonResponse({"status": "error", "message": "No options were loaded"})


def get_menu_items_from_menu(request):
    if request.htmx.request.method == "GET":
        menu_id = request.GET.get("menu_id")
        if menu_id == "all":
            menu_items = MenuItem.objects.all().prefetch_related("categories")
        else:
            menu_items = MenuItem.objects.filter(menus__id=menu_id).prefetch_related(
                "categories"
            )
        category_items = {}
        for item in menu_items:
            for category in item.categories.all():
                if category not in category_items:
                    category_items[category] = [item]
                else:
                    category_items[category].append(item)

        menus = Menu.objects.all()
        context = {"category_items": category_items, "menus": menus}
        back_button = request.GET.get("back", False)
        print(back_button)
        if back_button:

            return render(request, "order/order_menu_back_partial.html", context)
        else:
            return render(request, "order/order_menu_items_partial.html", context)


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "order/order_create_form.html"
    success_url = reverse_lazy("order_list")


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


class TicketListView(ListView):
    model = Ticket
    tempalte_name = "order/ticket_list.html"
    context_object_name = "tickets"


class TicketCreateView(JsonDeserializerMixin, View):
    template_name = "order/ticket_create_form.html"
    form_class = OrderItemFormSet

    def post(self, request, *args, **kwargs):

        if request.htmx:

            try:
                # Get JSON data from request
                data_str = request.POST.get("myVals", None)

                if data_str:
                    # Load string data into JSON
                    data = json.loads(data_str)
                    for ticket_data in data["myVals"]["tickets"]:
                        print(f"TICKET ID: {ticket_data['id']}")
                        ticket, created = Ticket.objects.update_or_create(
                            id=ticket_data["id"],
                            defaults={
                                "equipment": ticket_data.get("equipment"),
                                "status": ticket_data["status"],
                                "reservation": ticket_data.get(
                                    "reservation"
                                ),  # Handle None if necessary
                            },
                        )

                        order_items = []
                        for item_data in ticket_data["items"]:
                            print(f"ITEM DATA: {item_data}")
                            try:
                                menu_item = MenuItem.objects.get(id=item_data["id"])
                                # Create OrderItem only if MenuItem exists
                                order_item = OrderItem(
                                    item=menu_item,
                                    ticket=ticket,  # Directly use the ticket instance
                                    options=item_data["options"],
                                )
                                order_items.append(order_item)
                            except MenuItem.DoesNotExist:
                                print(
                                    f"Error: MenuItem with ID {item_data['id']} does not exist."
                                )

                        # Bulk create order items if any
                        if order_items:
                            OrderItem.objects.bulk_create(order_items)

                    return JsonResponse({"status": "successful"})

                else:
                    JsonResponse(
                        {"status": "error", "message": "No data passed"}, status=400
                    )

            except json.JSONDecodeError:
                return JsonResponse(
                    {"status": "error", "message": "Invalid JSON data."}, status=400
                )

        #     ticket_id = request.POST.get("ticket_id", None)

        #     if ticket_id is None:
        #         last_ticket = Ticket.objects.last()
        #         ticket_id = last_ticket.id

        #     item_ids = request.POST.get("myVals")
        #     data_dict = json.loads(item_ids)

        #     menu_id_list = data_dict["item_ids"].split(",")

        #     """melt the id strings into just ids that can be used to make order objects"""
        #     order_ids = {}
        #     for menu_id in menu_id_list:
        #         split_pos = menu_id.rfind("-") + 1
        #         order_id = int(menu_id[split_pos:])
        #         if order_id in order_ids:
        #             order_ids[order_id] += 1
        #         else:
        #             order_ids[order_id] = 0

        #     formset_data = {
        #         "form-TOTAL_FORMS": "0",
        #         "form-INITIAL_FORMS": "0",
        #         "form-MAX_NUM_FORMS": "",
        #     }
        #     for i, order_id in enumerate(order_ids):
        #         quantity = order_ids[order_id]

        #         formset_data[f"formset-string-{i}-id"] = order_id
        #         formset_data[f"formset_string-{i}-quantity"] = quantity
        #         formset_data[f"formset_string-{i}-ticket"] = ticket_id

        #     order_items_form = OrderItemFormSet(initial=formset_data)
        #     print(formset_data)
        #     if order_items_form.is_valid():
        #         print("valid formset")

        #     # if request.get("ticket_id") is None:
        #     #     last_ticket = Ticket.objects.last()
        #     #     last_ticket_id = last_ticket.id + 1 if last_ticket else 1

        #     # ticketform = TicketForm()
        #     # order_items = []

        #     # next_ticket_id = last_ticket.id + 1 if last_ticket else 1
        #     # menu_item_ids = request.POST.getlist("menu_items")
        #     # ticket_id = request.POST.get("ticket_id", None)

        #     # if ticket_id:
        #     #     ticket = Ticket.objects.filter(id=ticket_id)
        #     # else:

        #     #     Ticket.objects.create()

        # return JsonResponse(
        #     {"status": "success", "message": "Order created successfully!"}
        # )

        # ticket_form = TicketForm(
        #     {
        #         "status": "placed",
        #         "reservation": request.POST.get("reservation", None),
        #     }
        # )
        # if ticket_form.is_valid():

        #     order_item_formset = OrderItemFormSet(
        #         self.setup_formset(
        #             request=request,
        #             form=TicketForm({"status": "placed"}),
        #             formset=OrderItemFormSet(),
        #             keys=["item_id", "quantity"],
        #             formset_string="orderitem_set",
        #         )
        #     )

        #     if order_item_formset.is_valid():
        #         new_ticket = ticket_form.save(commit=False)
        #         instances = order_item_formset.save(commit=False)
        #         for instance in instances:
        #             instance.ticket = new_ticket
        #             instance.save()


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
