import requests
from config import ow_key
from datetime import datetime




def get_weather(city, ow_key):

    try:
        condition = {
            'Thunderstorm': 'Гроза ⛈',
            'Rain': 'Дождь 🌧',
            'Snow': 'Снег ☃',
            'Clear': 'Ясно ☀',
            'Clouds': 'Облачно ☁'
        }
        responce = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={ow_key}&units=metric')
        data = responce.json()
        now_date = datetime.fromtimestamp(data['dt'])
        city = city.title()
        temp = data['main']['temp']
        feellike = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        cond = data['weather'][0]['main']
        if cond in condition:
            cond = condition[cond]
        else:
            cond = 'Выгляни на улицу, там что-то необычное'
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        print(f'      Погода в {city} сегодня\n'
               f'Время: {now_date.hour}:{now_date.minute}:{now_date.second}\n'
               f'Температура: {temp} Cº {cond}\nОщущается как: {feellike} Cº\n'
               f'Влажность: {humidity} %\nАтмосферное давление: {pressure} мм.рт.ст\n'
               f'Скорость ветра: {wind_speed} м\\с\n'
               f'Рассвет в: {sunrise.hour}:{sunrise.minute}:{sunrise.second}\n'
               f'Заход солнца: {sunset.hour}:{sunset.minute}:{sunset.second}\n'
               f'Световой день: {sunset - sunrise}')
    except Exception:
        print('Проверь название города')


def main():
    city = input('Введите город: ')
    print()
    get_weather(city, ow_key)

if __name__ == '__main__':
    main()