from random import randint

a = int(input("Введите количество чисел: "))
b = int(input("Введите начало диапазона: "))
c = int(input("Введите конец диапазона: "))

with open("numsTask1.txt", 'w') as nums_file:
    for i in range(0, a):
        nums_file.write(f"{randint(b, c)} ")

with open("numsTask1.txt", 'r+') as nums_file:
    nums_arr = list(map(int, nums_file.readline().split()))
    print(nums_arr)

min_num = nums_arr[0]
min_i = 0
for i in range(len(nums_arr)):
    if nums_arr[i] < min_num:
        min_num = nums_arr[i]
        min_i = i
print(f"Минимальное число: {min_num}")
print(f"Индекс минимального числа: {min_i}")

mult_num = 1

while min_i != (len(nums_arr) - 1):
    min_i += 1
    mult_num *= nums_arr[min_i]
if mult_num == 1:
    print("Число для перемножения одно, поэтому не вышло(")
else:
    print(f"Полученное произведение: {mult_num}")
