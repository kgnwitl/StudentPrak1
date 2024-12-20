#from random import randint
from random import randint

def rand_num(n):
    arr_rand = []
    index = 0
    while index != n:
        num = randint(1, 32)
        flag = 0
        for index_j in range(len(arr_rand)):
            if num == arr_rand[index_j]:
                flag += 1
        if flag == 0:
            arr_rand.append(num)
            index += 1
    return arr_rand

with open("input.txt", 'w') as input_file:
    arr = rand_num(10)
    for _ in range(len(arr)):
        input_file.write(f"{arr[_]} ")
    a = int(input("Введите количество комбинаций: "))
    input_file.write(f"\n{a}")
    while a != 0:
        input_file.write("\n")
        arr_chance = rand_num(6)
        for _ in range(6):
            input_file.write(f"{arr_chance[_]} ")
        a -= 1
with open("input.txt", 'r') as output_input_file:
    win_str = output_input_file.readline()
    win_str = win_str.split()
    print(win_str)
    b = int(output_input_file.readline())
    print(f"n = {b}")
    array_input = dict()
    for i in range(0, b):
        input_str = output_input_file.readline()
        input_str = input_str.replace("\n", "")
        input_str = input_str.split()
        array_input.setdefault(i, input_str)
    f = 0

with open("output.txt", 'w') as output_file:
    for i in range(len(win_str)):
        output_file.write(f"{win_str[i]} ")
    output_file.write("\n")
    for i in range(0, b):
        array_input_str = array_input[i]
        fnum = 0
        for j in range(len(array_input_str)):
            if array_input_str[j] in win_str:
                fnum += 1
        if fnum >= 3:
            for _ in range(len(array_input[i])):
                output_file.write(f"{array_input[i][_]} ")
            output_file.write("- Lucky\n")

        else:
            for _ in range(len(array_input[i])):
                output_file.write(f"{array_input[i][_]} ")
            output_file.write("- Unlucky\n")