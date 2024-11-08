from random import uniform


def random_arr(num_a, num_b, num_n):
    arr = list(range(0, num_n))
    for _ in range(len(arr)):
        arr[_] = round(uniform(num_a, num_b), 5)
    return arr

a = int(input("Начало диапазона: "))
b = int(input("Конец диапазона: "))
n = int(input("Введите количество элементов массива: "))
random_num_array = random_arr(a, b, n)
print(f"Сгенерированный массив: {random_num_array}")

positive_arr = []
negative_arr = []
for i in range(len(random_num_array)):
    if random_num_array[i] >= 0:
        positive_arr.append(random_num_array[i])
    else:
        negative_arr.append(random_num_array[i])
print(f"Массив с положительными элементами: {positive_arr}")
print(f"Массив с отрицательными элементами: {negative_arr}")