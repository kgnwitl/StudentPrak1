def input_in_array(arr):
    input_array = " "
    while input_array != "":
        input_array = input("Введите строку в массив: ")
        arr.append(input_array)
    return arr

array_str = []
input_in_array(array_str)
array_str.pop(-1)
print(array_str)
max_str = array_str[0]
min_str = array_str[0]
for i in range(len(array_str)):
    if len(array_str[i]) > len(max_str):
        max_str = array_str[i]
    elif len(array_str[i]) < len(min_str):
        min_str = array_str[i]
print(f"Самая большая строка: {max_str}")
print(f"Самая короткая строка: {min_str}")