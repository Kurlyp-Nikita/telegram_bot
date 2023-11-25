import requests

# погода для 1-го дня.

def pogodaGorod(city_id):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    key = 'b5acdd7f46dc29237cec9d8e615405b3'

    params = {
        'id': city_id,
        'appid': key,
        'lang': 'ru',
        'units': 'metric'
    }

    try:
        result = requests.get(url, params=params, timeout=30)
        data = result.json()

        k1 = data["name"]
        k2 = data["main"]["temp"]
        k3 = data["wind"]["speed"]
        k4 = data["weather"][0]["description"]

        print(f'Погода в {k1}')
        print(f'Температура: {round(k2, 0)}°C {k4}')
        print(f'Ветер: {k3} м/с')
    except requests.exceptions.RequestException as e:
        print('Ошибка при выполнении запроса:', e)


pogodaGorod(500096)


# погода для 5-ти дней, на время которое мы можем указать.

def pogoda5d(city_id):
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    key = 'b5acdd7f46dc29237cec9d8e615405b3'

    params = {
        'id': 500096,
        'appid': key,
        'lang': 'ru',
        'units': 'metric'
    }

    try:
        result = requests.get(url, params=params, timeout=10)
        data = result.json()

        for one in data['list']:
            if '15:00' in one['dt_txt']:
                print(one['dt_txt'], one['main']['temp'], '°C', one['weather'][0]['description'])
    except requests.exceptions.RequestException as e:
        print('Ошибка при выполнении запроса:', e)


pogoda5d(500096)




