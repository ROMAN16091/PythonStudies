import requests
from django.conf import settings

class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_weather(city_name: str) -> dict:
        params = {
            'q': city_name,
            'appid': settings.OPENWEATHER_API_KEY,
            'units': 'metric',
            'lang': 'uk'
        }

        response = requests.get(WeatherService.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()