print("Введите строку в файл: ")

with open("numsTask2.txt", 'w') as nums_file:
    a = input()
    while a != "":
        nums_file.write(f"{a}\n")
        a = input()

with open("numsTask2.txt", 'r+') as nums_file:
    str_arr = nums_file.read()
    str_arr = str_arr.split()
fin_str = ""
for _ in range(len(str_arr)):
    fin_str += str_arr[_] + " "
print(fin_str)