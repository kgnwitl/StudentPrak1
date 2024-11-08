from random import randint

a = int(input("Введите количество чисел: "))
b = int(input("Введите начало диапазона: "))
c = int(input("Введите конец диапазона: "))

with open("numsTask3.txt", 'w') as nums_file:
    for i in range(0, a):
        nums_file.write(f"{randint(b, c)},")

with open("numsTask3.txt", 'r+') as nums_file:
    nums_arr = nums_file.readline()
    nums_arr = nums_arr.split(",")
    nums_arr.pop(len(nums_arr) - 1)

for i in range(len(nums_arr)):
    nums_arr[i] = int(nums_arr[i])
print(f"Числа из файла: {nums_arr}")

div = 0
max_plus_num = -1
min_plus_num = nums_arr[0]
for i in range(len(nums_arr)):
    if nums_arr[i] > 0:
        if nums_arr[i] > max_plus_num:
            max_plus_num = nums_arr[i]
        if nums_arr[i] < min_plus_num:
            min_plus_num = nums_arr[i]
div = max_plus_num - min_plus_num

print(f"Разница между самым большим и самым малым положительным числом: {div}")