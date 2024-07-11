from django.shortcuts import render
from .models import Driver, Race, Result

def home(request):
    return render(request, 'teams/home.html')

def drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'teams/drivers.html', {'drivers': drivers})

def races(request):
    races = Race.objects.all()
    return render(request, 'teams/races.html', {'races': races})

def results(request):
    results = Result.objects.all()
    return render(request, 'teams/results.html', {'results': results})
