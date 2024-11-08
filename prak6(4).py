def input_num_in_array(numarray):
    input_num_array = 1
    while input_num_array > 0:
        try:
            input_num_array = int(input("Введите число в массив: "))
        except ValueError:
            print("Некорректный ввод, попробуйте снова: ")
            continue
        numarray.append(input_num_array)
    return numarray

num_array = []
num_array = input_num_in_array(num_array)
num_array.pop()
print(num_array)

sum = 0
a = int(input("Введите число a: "))
for _ in range(len(num_array)):
    if num_array[_] % a == 0:
        sum += num_array[_]
print(f"Сумма: {sum}")
