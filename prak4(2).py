from random import uniform

a = int(input("Введите количество чисел: "))
b = int(input("Введите начало диапазона: "))
c = int(input("Введите конец диапазона: "))
with open("numsTask2.txt", 'w') as nums_file:
    for i in range(0, a):
        nums_file.write("{:.5f};".format(uniform(b, c)))
with open("numsTask2.txt", 'r+') as nums_file:
    nums_arr = nums_file.readline()
    nums_arr = nums_arr.split(";")
    nums_arr.pop()
nums_arr = list(map(float, nums_arr))
print(f"Числа из файла: {nums_arr}")
sum = 0
for i in range(len(nums_arr)):
    if round(nums_arr[i], 5) > round(0, 5):
        sum += round(nums_arr[i], 5)
print(f"Сумма: {round(sum, 5)}")