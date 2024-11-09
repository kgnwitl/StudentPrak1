def input_num_in_array(arr):
    input_num_array = 1
    while input_num_array != 0:
        try:
            input_num_array = int(input("Введите число в массив: "))
        except ValueError:
            print("Некорректный ввод, попробуйте снова: ")
            continue
        arr.append(input_num_array)
    return arr
def main():
    num_array = []
    input_num_in_array(num_array)
    num_array.pop(-1)
    print(f"Полученный массив: {num_array}")
    sum_num = 0
    mult = 1
    for i in range(len(num_array)):
        sum_num += num_array[i]
        mult *= num_array[i]

    middle_num = sum_num / len(num_array)
    print(f"Сумма: {sum_num}, Произведение: {mult}, Среднее в массиве: {middle_num}")

if __name__ == "__main__":
    main()