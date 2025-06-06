import requests, json

def get_weather_from_api(data, status_code):
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    if status_code == 200:
        return {
            "temp": temp,
            "description": description
        }, status_code
    else:
        return status_code


def test_get_weather_from_api():
    expected = ({"temp": 16.09, "description": 'рвані хмари'}, 200)
    actual = {
        "main": {"temp": 16.09},
        "weather": [{"description": "рвані хмари"}]
    }
    assert get_weather_from_api(actual, 200) == expected

if __name__ == '__main__':
    test_get_weather_from_api()
    print("Всі тести пройдено успішно!")
