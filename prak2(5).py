from random import randint
import calendar

def middle_temp(temp):
    sum_temp = 0
    for _ in range(len(temp)):
        sum_temp += temp[_]
    middle_temp_num = sum_temp / len(temp)
    return middle_temp_num

nums = dict()
for _ in range(12):
    weather_temperature = [randint(-10, 20) for _ in range(30)]
    nums[calendar.month_name[_+1]] = weather_temperature
for _ in range(len(nums)):
    print(f"{calendar.month_name[_+1]} - {nums[calendar.month_name[_+1]]}")
array_middle_num = dict()

for _ in range(len(nums)):
    array_middle_num[calendar.month_name[_+1]] = middle_temp(nums[calendar.month_name[_+1]])
print(f"\nСловарь средних температур: ")
for _ in range(len(nums)):
    print(f"{calendar.month_name[_+1]} - {round(array_middle_num[calendar.month_name[_+1]], 3)}")