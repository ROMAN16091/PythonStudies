from django.shortcuts import render
from .forms import CityForm
from .services import WeatherService

def index(request):
    weather_data = None
    form = CityForm(request.GET or None)
    if form.is_valid():
        city = form.cleaned_data['city']
        weather_data = WeatherService.get_weather(city)

    return render(request, 'weather/index.html', {
        'form': form,
        'weather': weather_data
    })

