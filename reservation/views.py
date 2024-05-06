from django.shortcuts import render, redirect
from .forms import ReservationForm, EventForm
from .models import Reservation, Event
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
    TemplateView,
)
from .mixins import ReservationMixin
from django.urls import reverse_lazy


# Create your views here.
class DashboardView(ReservationMixin, TemplateView):
    form_class = ReservationForm
    template_name = "reservation/dashboard.html"

    login_url = "/login/"
    redirect_field_name = "next"

    def get(self, request, *args, **kwargs):

        location_name, selected_date, reservation_status, selected_time = (
            self.process_reservation_data(request)
        )
        print(location_name, selected_date, reservation_status, selected_time)
        context = self.get_context_data(
            location_name=location_name,
            reservation_status=reservation_status,
            selected_time=selected_time,
            selected_date=selected_date,
        )

        if request.htmx:
            if __debug__:
                print("HTMX Request: Get partial reservation list")
            return render(
                request,
                "reservation/reservation_list_partial.html",
                {"reservations": context["reservations"]},
            )

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/success/")
        return self.get(request)


class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "reservation/reservation_create_form.html"
    success_url = reverse_lazy("reservation_list")  # Redirect after successful creation


class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "reservation/reservation_update_form.html"
    success_url = reverse_lazy(
        "reservation_detail"
    )  # Adjust to include primary key or correct redirection


class ReservationListView(ListView):
    model = Reservation
    template_name = "reservation/reservation_list.html"
    context_object_name = "reservations"


class ReservationDetailView(DetailView):
    model = Reservation
    template_name = "reservation/reservation_detail.html"


class DeleteReservation(DeleteView):
    model = Reservation
    template_name = "reservation/reservation_confirm_delete.html"
    success_url = reverse_lazy("reservation_list")


class CreateEvent(CreateView):
    model = Event
    form_class = EventForm
    template_name = "reservation/event_create_form.html"
    success_url = reverse_lazy("event_list")  # Redirect after successful creation


class UpdateEvent(UpdateView):
    model = Event
    form_class = EventForm
    template_name = "reservation/event_update_form.html"
    success_url = reverse_lazy(
        "event_detail"
    )  # Adjust to include primary key or correct redirection


class EventListView(ListView):
    model = Event
    template_name = "reservation/event_list.html"
    context_object_name = "events"


class EventDetailView(DetailView):
    model = Event
    template_name = "reservation/event_detail.html"


class DeleteEvent(DeleteView):
    model = Event
    template_name = "reservation/event_confirm_delete.html"
    success_url = reverse_lazy("event_list")
