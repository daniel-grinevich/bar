from django.shortcuts import render


# Create your views here.
def home(request):

    if request.htmx:
        print('HTMX request')
    else:
        print('Not a HTMX request')
    
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')

def menu(request):
    return render(request, 'core/menu.html')

def contact(request):
    return render(request, 'core/contact.html')

def wineclub(request):
    return render(request, 'core/wineclub.html')

def reservation(request):
    return render(request, 'core/reservation.html')