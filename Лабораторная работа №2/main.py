from get_weather import get_weather_data

MY_KEY = 'секрет)' # Константа

if __name__ == '__main__':
    city = input() # ввод города
    result = get_weather_data(city, MY_KEY)
    print(result)