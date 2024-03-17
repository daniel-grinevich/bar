from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'reservation/dashboard.html')


def reservation(request):
    return render(request, 'reservation/reservation.html')