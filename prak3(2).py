from random import randint

a = int(input("Введите количество чисел: "))
b = int(input("Введите начало диапазона: "))
c = int(input("Введите конец диапазона: "))
with open("nums.txt", 'w') as nums_file:
    for i in range(0, a):
        nums_file.write(f"{randint(b, c)} ")
with open("nums.txt", 'r+') as nums_file:
    nums_arr = nums_file.readline()
    nums_arr = nums_arr.split()
    print(nums_arr)
    for i in range(len(nums_arr)):
        nums_arr[i] = int(nums_arr[i])
    print(nums_arr)
    b = len(nums_arr)
    i = 0
    while b != 0:
        if nums_arr[i] % 2 == 0:
            nums_arr.pop(i)
        else:
            i += 1
        b -= 1
    print(nums_arr)

with open("nums.txt", 'w') as nums_file:
    for i in range(len(nums_arr)):
        nums_file.write(f"{nums_arr[i]} ")