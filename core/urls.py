# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/',views.menu, name='menu'),
    path('contact/',views.menu, name='contact'),
    path('wineclub/',views.wineclub, name='wineclub'),
]
