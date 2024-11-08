from random import randint

def random_mass(inputA, inputB, inputN):
    random_num_mass = list(range(0, inputN))
    i = 0
    for _ in range(len(random_num_mass)):
        random_num_mass[_] = randint(inputA, inputB)
    return random_num_mass

inputA = int(input("Начало диапазона: "))
inputB = int(input("Конец диапазона: "))
inputN = int(input("Введите количество элементов массива: "))
random_num_array = random_mass(inputA, inputB, inputN)
for _ in range(len(random_num_array)):
    print(f"\t{_} -> {random_num_array[_]}")
