from django.shortcuts import render, redirect
from .forms import CustomerReservationForm, ReservationForm



# Create your views here.
def dashboard(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success/')
        else:
            form = ReservationForm()
    return render(request, 'reservation/dashboard.html', {'form': form})


def create(request):
    if request.method == 'POST':
        form = CustomerReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success/')
        else:
            form = CustomerReservationForm()

    return render(request, 'reservation/create.html', {'form': form})
