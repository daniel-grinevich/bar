# Inside your reservations app, forms.py
from django import forms
from .models import Reservation, Event


class CustomerReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "event",
            "number_of_people",
            "start_time",
            "end_time",
            "special_requests",
        ]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "event",
            "number_of_people",
            "start_time",
            "end_time",
            "custom_user",
            "status",
            "special_requests",
            "deposit_paid",
            "source",
            "location",
            "table",
        ]  # Specify the fields you want in the form


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "cover"]
