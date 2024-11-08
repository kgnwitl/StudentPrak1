n = int(input("Введите число n: "))
random_array = [[1 for _ in range(n)] for _ in range(n)]

for _ in range(len(random_array)):
    print(random_array[_])
print()
for i in range(1, len(random_array)):
    for j in range(1, len(random_array[i])):
        random_array[i][j] = random_array[i - 1][j] + random_array[i][j - 1]

for i in range(len(random_array)):
    for j in range(len(random_array[i])):
        print(f"{random_array[i][j]}\t", end="")
    print()