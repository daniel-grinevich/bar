from django.utils import timezone
from location.models import Location, Table
from .models import Reservation
import math
import datetime


def convert_interger_to_time(time_integer):
    time = int(time_integer)
    hours = math.floor(time / 60)
    mins = time % 60

    return datetime.time(hour=hours, minute=mins)


class ReservationMixin:
    def process_reservation_data(self, request):
        location_name = request.GET.get("locationSelector", None)
        selected_date = request.GET.get(
            "dateInput", timezone.now().date().strftime("%Y-%m-%d")
        )
        reservation_status = request.GET.get("reservationStatus", "pending")
        selected_time = request.GET.get("timeInput", timezone.now().time())

        return location_name, selected_date, reservation_status, selected_time

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        current_time = timezone.now()
        context["prepopulate_date_input_fields"] = current_time.date().strftime(
            "%Y-%m-%d"
        )
        location_name = kwargs.get("location_name", "Default Location")
        reservation_status = kwargs.get("reservation_status", "pending")
        selected_date = kwargs.get("selected_date", current_time)
        selected_time = kwargs.get("selected_time")

        if not isinstance(selected_time, datetime.time):
            combine_time = convert_interger_to_time(selected_time)
            combine_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d").date()
            time = datetime.datetime.combine(combine_date, combine_time)

        if selected_date and location_name and reservation_status and time:
            context["reservations"] = Reservation.get_reservation_list(
                selected_date, location_name, reservation_status, time
            )
        else:
            context["reservations"] = Reservation.objects.all()

        context["locations"] = Location.objects.all()
        context["tables"] = (
            Table.objects.filter(location__name=location_name)
            if location_name
            else Table.objects.all()
        )

        return context
