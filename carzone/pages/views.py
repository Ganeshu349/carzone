from django.http import HttpResponse
from django.shortcuts import render
from .models import team

# Create your views here.
def home(request):
    teams = team.objects.all()
    data = {
        'teams' : teams,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = team.objects.all()
    data = {
        'teams' : teams
    }
    return render(request, 'pages/about.html')

def service(request):
    return render(request, 'pages/service.html')

def contact(request):
    return render(request, 'pages/contact.html')

# def cars(request):
#     return render(request, 'cars/cars.html')