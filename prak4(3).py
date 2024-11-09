from random import randint

a = int(input("Введите количество чисел: "))
b = int(input("Введите начало диапазона: "))
c = int(input("Введите конец диапазона: "))

with open("numsTask3.txt", 'w') as nums_file:
    for i in range(0, a):
        nums_file.write(f"{randint(b, c)},")

with open("numsTask3.txt", 'r+') as nums_file:
    nums_arr = nums_file.readline().split(",")
    nums_arr.pop(len(nums_arr) - 1)
nums_arr = list(map(int, nums_arr))
print(nums_arr)
div = 0

positiv_arr = []
for i in range(len(nums_arr)):
    if nums_arr[i] > 0:
        positiv_arr.append(nums_arr[i])
print("Массив положительных чисел: ", positiv_arr)
max_plus_num = positiv_arr[0]
min_plus_num = positiv_arr[0]
for i in range(len(positiv_arr)):
    if max_plus_num < positiv_arr[i]:
        max_plus_num = positiv_arr[i]
    if min_plus_num > positiv_arr[i]:
        min_plus_num = positiv_arr[i]

div = max_plus_num - min_plus_num

print(f"Разница между самым большим и самым малым положительным числом: {div}")