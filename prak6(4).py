def input_num_in_array():
    input_num_array = 1
    arr = []
    while input_num_array >= 0:
        try:
            input_num_array = int(input("Введите число в массив: "))
        except ValueError:
            print("Некорректный ввод, попробуйте снова: ")
            continue
        arr.append(input_num_array)
    return arr

num_array = input_num_in_array()
num_array.pop()
print(num_array)

sum_num = 0
a = int(input("Введите число a: "))
for _ in range(len(num_array)):
    if num_array[_] % a == 0:
        sum_num += num_array[_]
print(f"Сумма: {sum_num}")
