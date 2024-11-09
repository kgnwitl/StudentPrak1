from random import uniform

a = int(input("Введите количество чисел: "))
b = int(input("Введите начало диапазона: "))
c = int(input("Введите конец диапазона: "))

with open("numsTask2.txt", 'w') as nums_file:
    for i in range(0, a):
        nums_file.write("{:.5f};".format(uniform(b, c)))

with open("numsTask2.txt", 'r+') as nums_file:
    nums_arr = nums_file.readline()
    buff_str = nums_arr
    nums_arr = nums_arr.split(";")
    nums_arr.pop(len(nums_arr) - 1)
nums_arr = list(map(float, nums_arr))
print(f"Числа из файла: {nums_arr}")

for i in range(len(nums_arr)):
    for j in range(len(nums_arr)):
        if nums_arr[i] < nums_arr[j]:
            nums_arr[i], nums_arr[j] = nums_arr[j], nums_arr[i]

print(f"Отсортированная последовательность: {nums_arr}")

with open("numsTask2.txt", 'w') as nums_file:
    nums_file.write(f"{buff_str}\n")
    for i in range(len(nums_arr)):
        nums_file.write(f"{nums_arr[i]};")


