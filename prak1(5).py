input_str = input("Введите строку: ")
num_word = 1
for i in range(len(input_str)):
    char = input_str[i]
    if char == " ":
        num_word += 1
print(f"Количество слов: {num_word}")
input_str = "Start " + input_str + " End"
print(f"Изменённая строка: {input_str}")
