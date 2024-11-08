def input_in_array(array):
    input_array = " "
    while input_array != "":
        input_array = input("Введите строку в массив: ")
        array.append(input_array)
    return array
array = []
input_in_array(array)
array.pop(-1)
print(array)
max = ""
min = array[0]
for i in range(len(array)):
    if len(array[i]) > len(max):
        max = array[i]
    if len(array[i]) < len(min):
        min = array[i]
print(f"Самая большая строка: {max}")
print(f"Самая короткая строка: {min}")