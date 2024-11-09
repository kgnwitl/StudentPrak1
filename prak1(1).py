import sys
from random import randint

def input_rand_num_a():
    try:
        a = int(input("Введите число, от которого будут случайные числа: "))
    except ValueError:
        print("Некорректный ввод, попробуйте снова: ")
        input_rand_num_a()
    return a

def input_rand_num_b():
    try:
        b = int(input("Введите число, до которого будут случайные числа: "))
    except ValueError:
        print("Некорректный ввод, попробуйте снова: ")
        input_rand_num_b()
    return b

a = input_rand_num_a()
b = input_rand_num_b()

NumArray = [randint(a, b) for _ in range(0, 10)]
print(f"Полученный массив: {NumArray}")
min = NumArray[0]
for i in range(len(NumArray)):
    if NumArray[i] <= min:
        min = NumArray[i]
print(f"Минимальное число в массиве: {min}")
