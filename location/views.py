from django.shortcuts import render
from django.views.generic import CreateView
from .models import Location, Table


def dashboard(request):
    pass


def detail(request):
    pass


class CreateLocation(CreateView):
    model = Location


class CreateTable(CreateView):
    model = Table
