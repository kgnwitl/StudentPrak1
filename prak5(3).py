from random import randint

a = int(input("Введите количество чисел: "))
b = int(input("Введите начало диапазона: "))
c = int(input("Введите конец диапазона: "))

with open("numsTask3.txt", 'w') as nums_file:
    for i in range(0, a):
        nums_file.write(f"{randint(b, c)} ")

with open("numsTask3.txt", 'r+') as nums_file:
    nums_arr = nums_file.readline()
    nums_arr = nums_arr.split()

for i in range(len(nums_arr)):
    nums_arr[i] = int(nums_arr[i])
print(nums_arr)

min_num = nums_arr[0]
min_i = 0
for i in range(len(nums_arr)):
    if nums_arr[i] < min_num:
        min_num = nums_arr[i]
        min_i = i
print(f"Минимальное число: {min_num}")
print(f"Индекс минимального числа: {min_i}")

i = 0
sum = 0
while i != (min_i):
    sum += nums_arr[i]
    i += 1
middle_num = sum / (min_i)
print(f"Среднее значение до {min_num}: ", middle_num)