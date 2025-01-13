import get_weather
import pytest


my_key = 'секрет)' # Константа

def test_without_key():
    assert get_weather.get_weather_data(
        "moscow") is None, \
        "Для получения данных необходимо задать значение для ключа"


def test_in_spb():
    assert get_weather.get_weather_data("Saint Petersburg",
                                           api_key=my_key) is not None, \
        "Тип ответа не соответствует"


def test_type_of_res():
    assert type(get_weather.get_weather_data("Riga",
                                                api_key=my_key)) is str, \
        "Тип ответа не соответствует"


def test_without_key():
    assert get_weather.get_weather_data(
        '') is None, \
        "Отсутствует ключ"


def test_without_city():
    assert get_weather.get_weather_data('',
                                           api_key=my_key) is None, \
        "Отсутствует название города"


def test_coord():
    import json
    assert len(
        json.loads(get_weather.get_weather_data('Riga', api_key=my_key)).get('coord')) == 2, \
        "Неправильные координаты: их должно быть дву"


def test_temp_type():
    import json
    assert type(json.loads(get_weather.get_weather_data('Riga', api_key=my_key)).get(
        'feels_like')) is float, \
        "Ошибка в типе значения температуры"