from django.shortcuts import render, redirect
from .forms import ReservationForm
from location.models import Location, Table
from .models import Reservation
from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class DashboardView(View):
    form_class = ReservationForm
    template_name = "reservation/dashboard.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        locations = Location.objects.all()
        tables = Table.objects.all()
        reservations = Reservation.get_week_of_reservations()

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


class CreateReservation(CreateView, LoginRequiredMixin):
    model = Reservation
    form_class = ReservationForm

    login_url = "/login/"
    # Optionally, specify the name of the GET parameter that the login view will use to
    # redirect the user back to this view after successful login. The default is 'next'.
    redirect_field_name = "next"
