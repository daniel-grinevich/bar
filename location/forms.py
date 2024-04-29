from .models import Location, Table
from django import forms


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "default"]


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ["name", "chairs", "available", "style", "location"]
