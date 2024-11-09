from random import randint

a = int(input("Введите количество чисел: "))
b = int(input("Введите начало диапазона: "))
c = int(input("Введите конец диапазона: "))

with open("numsTask5.txt", 'w') as nums_file:
    for i in range(0, a):
        nums_file.write(f"{randint(b, c)} ")

with open("numsTask5.txt", 'r+') as nums_file:
    nums_arr = nums_file.readline().split()
nums_arr = list(map(int, nums_arr))

print(nums_arr)

min_num = nums_arr[0]
max_num = nums_arr[0]
min_i = 0
max_i = 0

for i in range(len(nums_arr)):
    if nums_arr[i] > max_num:
        max_num = nums_arr[i]
        max_i = i
    if nums_arr[i] < min_num:
        min_num = nums_arr[i]
        min_i = i

print(f"Минимальное число: {min_num}, Его индекс: {min_i}")
print(f"Максимальное число: {max_num}, Его индекс: {max_i}")

sum_num = 0
k = 0

if min_i > max_i:
    max_i += 1
    while max_i != min_i:
        sum_num += nums_arr[max_i]
        k += 1
        max_i += 1
elif max_i > min_i:
    min_i += 1
    while min_i != max_i:
        sum_num += nums_arr[min_i]
        k += 1
        min_i += 1
if k == 0:
    print("между числами нет чисел.")
else: print(f"Среднее арифметическое: {round(sum_num / k, 4)}")

