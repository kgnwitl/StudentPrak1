def InputNumInArray(NumArray):
    input_num_array = 1
    while input_num_array != 0:
        try:
            input_num_array = int(input("Введите число в массив: "))
        except ValueError:
            print("Некорректный ввод, попробуйте снова: ")
            continue
        NumArray.append(input_num_array)
    return NumArray

NumArray = []
InputNumInArray(NumArray)
NumArray.pop(-1)
print(f"Полученный массив: {NumArray}")
sum = 0
mult = 1
for i in range(len(NumArray)):
    sum += NumArray[i]
    mult *= NumArray[i]

middlenum = sum / len(NumArray)
print(f"Сумма: {sum}, Произведение: {mult}, Среднее в массиве: {middlenum}")