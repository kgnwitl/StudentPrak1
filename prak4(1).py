num = int(input("Введите целом натуральное число: "))

digit = 3
mult_num = 1

while mult_num <= num:
    mult_num *= digit
    if mult_num > num:
        mult_num //= digit
        break
    digit += 3
print(mult_num)