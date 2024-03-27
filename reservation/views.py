from django.shortcuts import render, redirect
from .forms import ReservationForm
from location.models import Location, Table
from .models import Reservation
from django.views.generic import View, CreateView, UpdateView


# Create your views here.
class DashboardView(View):
    form_class = ReservationForm
    template_name = "reservation/dashboard.html"

    login_url = "/login/"
    redirect_field_name = "next"

    def get(self, request, *args, **kwargs):

        location_name = request.GET.get("location", None)
        selected_date = request.GET.get("dateInput", None)

        if location_name is None:
            default_location = Location.objects.get(default=True)
            location_name = default_location.name

        reservations = (
            Reservation.get_reservation_location_date(selected_date, location_name)
            if selected_date and location_name
            else Reservation.objects.all()
        )

        if request.htmx:
            if __debug__:
                print("HTMX Request: Get partial reservation list")
            return render(
                request,
                "reservations/reservation_list_partial.html",
                {"reservations": reservations},
            )

        form = self.form_class()
        locations = Location.objects.all()
        tables = (
            Table.objects.filter(location__name=location_name)
            if location_name
            else Table.objects.all()
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
