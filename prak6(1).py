print("Введите строку в файл: ")

with open("numsTask1.txt", 'w') as nums_file:
    nums_file.write(f"{input()} ")

with open("numsTask1.txt", 'r+') as nums_file:
    str_arr = nums_file.readline()
    str_arr = str_arr.split()

for i in range(len(str_arr)):
    if len(str_arr[i]) % 2 != 0:
        print(str_arr[i])