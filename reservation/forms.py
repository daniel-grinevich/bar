# Inside your reservations app, forms.py
from django import forms
from .models import Reservation


class CustomerReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'event',
            'number_of_people',
            'date',
            'start_time',
            'end_time',
            'special_requests',
        ]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'event',
            'number_of_people',
            'date',
            'start_time',
            'end_time',
            'custom_user',
            'status',
            'location',
            'special_requests',
            'staff',
            'deposit_paid',
            'source'
        ]  # Specify the fields you want in the form
