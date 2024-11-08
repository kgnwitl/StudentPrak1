num_len_array = int(input("Введите длину массива: "))
num_array = [0 for _ in range(num_len_array)]
num = 1
for _ in range(len(num_array)):
    num_array[_] = num
    num += 2
print(num_array)