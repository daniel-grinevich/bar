from django.shortcuts import render, redirect
from .forms import ReservationForm
from location.models import Location, Table
from .models import Reservation
from django.views.generic import View, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class DashboardView(LoginRequiredMixin, View):
    form_class = ReservationForm
    template_name = "reservation/dashboard.html"

    login_url = "/login/"
    redirect_field_name = "next"

    def get(self, request, *args, **kwargs):
        location_name = request.Get.get("location", None)
        date_range = request.Get.get("date_ranage", None)
        form = self.form_class()
        locations = Location.objects.all()
        tables = (
            Table.objects.filter(location__name=location_name)
            if location_name
            else Table.objects.all()
        )
        reservations = (
            Reservation.get_week_of_reservations(date_range, location_name)
            if date_range and location_name
            else Reservation.objects.all()
        )

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "locations": locations,
                "tables": tables,
                "reservations": reservations,
            },
        )

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
