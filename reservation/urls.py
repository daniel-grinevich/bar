# core/urls.py
from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('details/<int:pk>/', views.details, name='details'),  # Updated path
    path('create/', views.create, name='create')
]
