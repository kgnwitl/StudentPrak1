from random import randint

a = int(input("Введите количество чисел: "))
b = int(input("Введите начало диапазона: "))
c = int(input("Введите конец диапазона: "))

with open("numsTask4.txt", 'w') as nums_file:
    for i in range(0, a):
        nums_file.write(f"{randint(b, c)} ")

with open("numsTask4.txt", 'r+') as nums_file:
    nums_arr = nums_file.readline()
    nums_arr = nums_arr.split()

for i in range(len(nums_arr)):
    nums_arr[i] = int(nums_arr[i])
print(nums_arr)

max_num = nums_arr[0]
for i in range(len(nums_arr)):
    if nums_arr[i] > max_num:
        max_num = nums_arr[i]
print(f"Максимальное число: {max_num}")

sum = 0
for i in range(len(nums_arr)):
    if nums_arr[i] == (max_num - 1):
        sum += nums_arr[i]
print("Сумма чисел, которая меньше максимального на 1: ", sum)
