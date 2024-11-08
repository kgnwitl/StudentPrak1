from random import randint

def middle_temp(temp):
    sum_temp = 0
    for _ in range(len(temp)):
        sum_temp += temp[_]
    middle_temp_num = sum_temp / len(temp)
    return middle_temp_num

weather_temperature = [[randint(-10, 20) for _ in range(30)] for _ in range(12)]
nums = dict()
for _ in range(len(weather_temperature)):
    nums.setdefault(_, weather_temperature[_])
print(nums)

array_middle_num = dict()

for _ in range(len(nums)):
    array_middle_num.setdefault(_, middle_temp(nums[_]))
print(f"Словарь средних температур: {array_middle_num}")