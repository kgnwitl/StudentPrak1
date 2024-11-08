import json
from datetime import datetime

import requests
import os

def check_file(): #проверка файна на наличие и чтение файла в массив
    if os.path.exists("weather.json"):
        with open("weather.json", 'r') as taskjson:
            try:
                name = json.load(taskjson)
            except json.JSONDecodeError:
                name = []
    else:
        name = []
    return name

def check_weather_city(city):
    useless_keys = ["timezone", "id", "cod", "sys", "clouds", "wind", "visibility", "base", "coord"]
    api_key = "bb407be874baca0c068315d0d20e8f11"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&date=&units=metric&lang=ru&APPID={api_key}"
    data = requests.get(url).json()
    times = datetime.now()
    data_with_time = {
        "time": f"{times.year}-{times.month}-{times.day} {times.hour}:{times.minute}"
    }
    arr_weather = check_file()

    for key in useless_keys:
        if key in data:
            del data[key]
    data.update(data_with_time)
    print("-------------------------------")
    print(f"Cейчас температура в {city}: {data["main"]["temp"]}°C, ощущается как: {data["main"]["feels_like"]}°C")
    print(f"На улице: {data["weather"][0]["description"]}")
    arr_weather.append(data)
    with open("weather.json", 'w') as weather_json:
        json.dump(arr_weather, weather_json, indent=4, ensure_ascii=False)

def delete_json():
    with open("weather.json", 'w') as delete:
        print("Файл очищен")

def default_city(mode):
    if mode == 1:
        json_arr = check_file()
        def_city = ''
        flag = 0
        for _ in range(len(json_arr)):
            if "def_city" in json_arr[_]:
                def_city = json_arr[_]["def_city"]
                flag += 1
        if def_city == '':
            def_city = input("Введите название города по умолчанию: ")
            print(f"Теперь, {def_city}, ваш город по умолчанию!")
        if flag == 0:
            def_dict = {
                'def_city': f'{def_city}'
            }
            json_arr.append(def_dict)
            with open("weather.json", 'w') as weather_json:
                json.dump(json_arr, weather_json, indent=4, ensure_ascii=False)
        elif flag == 1:
            check_weather_city(def_city)

    elif mode == 2:
        json_arr = check_file()
        for i in range(len(json_arr)):
            if "def_city" in json_arr[i]:
                json_arr.pop(i)
                break
        def_city = input("Введите название города по умолчанию: ")
        print(f"Теперь, {def_city}, ваш город по умолчанию!")
        def_dict = {
            'def_city': f'{def_city}'
        }
        json_arr.append(def_dict)
        with open("weather.json", 'w') as weather_json:
            json.dump(json_arr, weather_json, indent=4, ensure_ascii=False)


def view_json():
    json_arr = check_file()
    for i in range(len(json_arr)):
        if "def_city" not in json_arr[i]:
            print("-------------------------------")
            print(f"Дата создания запроса: {json_arr[i]["time"]}")
            print(f"Температура в {json_arr[i]["name"]}: {json_arr[i]["main"]["temp"]}°C, ощущается как: {json_arr[i]["main"]["feels_like"]}°C")
            print(f"На улице: {json_arr[i]["weather"][0]["description"]}")


def main():
    num_input_var = 1
    while num_input_var != 0:
        print("-------------------------------")
        print("Погода в городе по умолчанию:")
        default_city(mode = 1)
        print("-------------------------------")
        print("Посмотреть погоду в населенном пункте: 1")
        print("Очистить историю запросов: -1")
        print("Сохранить город по умолчанию: 2")
        print("Посмотреть историю запросов: 3")
        print("Выход - 0")

        print("Выберите действие: ", end="")
        try: num_input_var = int(input())
        except ValueError:
            print("Некорректный ввод, попробуйте снова")
            continue
        if num_input_var == 1: check_weather_city(city = input("Введите город: "))
        if num_input_var == -1: delete_json()
        if num_input_var == 2: default_city(mode = 2)
        if num_input_var == 3: view_json()

    print("-------------------------------")
    print("До свидания!")

if __name__ == "__main__":
    main()