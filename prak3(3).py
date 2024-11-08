from random import randint

a = int(input("Введите количество чисел: "))
c = int(input("Введите конец диапазона: "))
with open("nums_prak3.txt", 'w') as nums_file:
    for i in range(0, a):
        nums_file.write(f"{randint(1, c)} ")
with open("nums_prak3.txt", 'r+') as nums_file:
    nums_arr = nums_file.readline()
    nums_arr = nums_arr.split()

print(f"Высоты: ", end="")
for i in range(len(nums_arr)):
    nums_arr[i] = int(nums_arr[i])
    print(f"{nums_arr[i]}\t", end="")
print()
max_s = 0
max_i = 0
max_j = 0
for i in range(len(nums_arr)):
    j = i
    S = 0
    while j != len(nums_arr) - 1:
        j += 1
        height = nums_arr[i]
        if nums_arr[i] >= nums_arr[j]:
            height = nums_arr[j]
        S = height * (j - i)
        if S > max_s:
            max_s = S
            max_i = i
            max_j = j
print(f"Самая большая площадь: {max_s}, i = {max_i}, j = {max_j}")



