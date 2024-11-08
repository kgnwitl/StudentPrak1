num = int(input("Введите число, с которого будут высчитываться 3: "))
num_array = [0 for _ in range(100)]
for _ in range(100):
    num_array[_] = num
    num -= 3
print(num_array)