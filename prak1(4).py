from random import randint

def random_mass(num_a, num_b, num_n):
    random_num_mass = list(range(0, num_n))
    i = 0
    for _ in range(len(random_num_mass)):
        random_num_mass[_] = randint(num_a, num_b)
    return random_num_mass

input_a = int(input("Начало диапазона: "))
input_b = int(input("Конец диапазона: "))
input_n = int(input("Введите количество элементов массива: "))
random_num_array = random_mass(input_a, input_b, input_n)
for _ in range(len(random_num_array)):
    print(f"\t{_} -> {random_num_array[_]}")
