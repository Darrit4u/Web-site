from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = 'd305a1fb6e61dd9ae8edddb32ce16872'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        if 'send' in request.POST:
            form = CityForm(request.POST)
            form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name), verify=False).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)


def delete(request, name):
    city = City.objects.filter(name=name)
    city.delete()
    return HttpResponseRedirect("/weather")

