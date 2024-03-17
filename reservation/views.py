from django.shortcuts import render, redirect
from .forms import CustomerReservationForm, ReservationForm


# Create your views here.
def dashboard(request):
    return render(request, 'reservation/dashboard.html')


def create(request):
    if request.method == 'POST':
        form = CustomerReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success/')
        else:
            form = CustomerReservationForm()

    return render(request, 'reservation/create.html', {'form': form})
