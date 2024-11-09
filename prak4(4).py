from random import randint

a = int(input("Введите количество чисел: "))
b = int(input("Введите начало диапазона: "))
c = int(input("Введите конец диапазона: "))

with open("numsTask4.txt", 'w') as nums_file:
    for i in range(0, a):
        nums_file.write(f"{randint(b, c)} ")
    #nums_file.write(f"1 1 2 2 2 4 4 4 5 5")

with open("numsTask4.txt", 'r+') as nums_file:
    nums_arr = list(map(int, nums_file.readline().split()))

print(f"Числа из файла: {nums_arr}")

count = 0
for i in range(1, len(nums_arr)):
    if nums_arr[i] == nums_arr[i - 1]:
        count += 1
print(count)
