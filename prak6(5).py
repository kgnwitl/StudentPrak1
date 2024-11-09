from random import randint

n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
num_arr = [[randint(0, 1) for _ in range(m)] for _ in range(n)]

print("Исходный массив: ")
for _ in range(len(num_arr)):
    print(num_arr[_])

for i in range(len(num_arr)):
    sum_num = 0
    for j in range(len(num_arr[i])):
        sum_num += num_arr[i][j]
    if sum_num % 2 != 0:
        num_arr[i].append(1)

print("Изменённый массив: ")
for _ in range(len(num_arr)):
    print(num_arr[_])
