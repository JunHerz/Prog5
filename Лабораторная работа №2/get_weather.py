import requests # чтобы выполнять запрос
import json # для демонстрации полученных данных

def format_utc(timezone):
    hours_offset = timezone // 3600  # Преобразуем смещение в секундах в часы
    return f"UTC{'+' if hours_offset >= 0 else ''}{hours_offset}" # Форматируем строку в вид UTC±N


def get_weather_data(place, api_key=None): # функция получения информации
    if not api_key: # обработка случаев
        return None
    if not place:
        return None
    url = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric'
    r = requests.get(url).json()
    city_info = {
        'name': r['name'],
        'country_code': r['sys']['country'],
        'coord': {
            'lon': r['coord']['lon'],
            'lat': r['coord']['lat']
        },
        'timezone': format_utc(r['timezone']),
        'temperature': r['main']['temp'],
        'feels_like': r['main']['feels_like']
    }
    res = json.dumps(city_info, ensure_ascii=False, indent=2)

    return res
