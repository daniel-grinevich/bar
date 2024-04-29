from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
    TemplateView,
)
from .models import Location, Table
from .forms import LocationForm, TableForm
from django.urls import reverse_lazy


class Dashboard(TemplateView):
    template_name = "location/dashboard.html"


class LocationCreateView(CreateView):
    model = Location
    template_name = "location/location_create_form.html"
    form_class = LocationForm


class LocationListView(ListView):
    model = Location
    template_name = "location/location_list.html"
    context_object_name = "locations"


class LocationDetailView(DetailView):
    model = Location
    template_name = "location/location_detail.html"


class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = "location/location_update_form.html"
    success_url = "/locations/"  # Redirect URL after a successful update


class LocationDeleteView(DeleteView):
    model = Location
    template_name = "location/location_confirm_delete.html"
    success_url = reverse_lazy("location_list")


class TableCreateView(CreateView):
    model = Table
    template_name = "location/table_create_form.html"
    form_class = TableForm


class TableListView(ListView):
    model = Table
    template_name = "location/table_list.html"
    context_object_name = "tables"


class TableDetailView(DetailView):
    model = Table
    template_name = "location/table_detail.html"


class TableUpdateView(UpdateView):
    model = Table
    form_class = TableForm
    template_name = "location/table_update_form.html"
    success_url = "/tables/"


class TableDeleteView(DeleteView):
    model = Table
    template_name = "location/table_confirm_delete.html"
    success_url = reverse_lazy("table_list")
