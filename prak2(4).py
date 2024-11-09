from random import randint

def middle_temp(temp):
    sum_temp = 0
    for _ in range(len(temp)):
        sum_temp += temp[_]
    middle_temp_num = sum_temp / len(temp)
    return middle_temp_num

weather_temperature = [[randint(-10, 20) for _ in range(30)] for _ in range(12)]

for _ in range(len(weather_temperature)):
    print(weather_temperature[_])
array_middle_num = []

for _ in range(len(weather_temperature)):
    array_middle_num.append(middle_temp(weather_temperature[_]))
print(f"Массив средних температур: ", end = "")
for _ in range(len(array_middle_num)):
    print(round(array_middle_num[_], 3), end = " ")

for i in range(len(array_middle_num)):
    for j in range(i, len(array_middle_num)):
        if array_middle_num[i] > array_middle_num[j]:
            array_middle_num[i], array_middle_num[j] = array_middle_num[j], array_middle_num[i]
print(f"\nМассив средних температур, упорядоченны по возрастанию: ", end = "")
for _ in range(len(array_middle_num)):
    print(round(array_middle_num[_], 3), end = " ")
