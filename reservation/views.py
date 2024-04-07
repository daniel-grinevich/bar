from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation
from django.views.generic import View, CreateView, UpdateView
from .mixins import ReservationMixin


# Create your views here.
class DashboardView(ReservationMixin, View):
    form_class = ReservationForm
    template_name = "reservation/dashboard.html"

    login_url = "/login/"
    redirect_field_name = "next"

    def get(self, request, *args, **kwargs):

        location_name, selected_date, reservation_status, selected_time = (
            self.process_reservation_data(request)
        )
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


class CreateReservation(CreateView):
    model = Reservation
    form_class = ReservationForm


class UpdateReservation(UpdateView):
    model = Reservation
