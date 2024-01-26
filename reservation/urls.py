# core/urls.py
from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
