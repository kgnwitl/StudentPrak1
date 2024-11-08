import sys
from random import randint

def InputRandNumA():
    try:
        a = int(input("Введите число, от которого будут случайные числа: "))
    except ValueError:
        print("Некорректный ввод, попробуйте снова: ")
        InputRandNumA()
    return a

def InputRandNumB():
    try:
        b = int(input("Введите число, до которого будут случайные числа: "))
    except ValueError:
        print("Некорректный ввод, попробуйте снова: ")
        InputRandNumB()
    return b

a = InputRandNumA()
b = InputRandNumB()

NumArray = [randint(a, b) for _ in range(0, 10)]
print(f"Полученный массив: {NumArray}")
min = sys.maxsize
for i in range(len(NumArray)):
    if NumArray[i] <= min:
        min = NumArray[i]
print(f"Минимальное число в массиве: {min}")
