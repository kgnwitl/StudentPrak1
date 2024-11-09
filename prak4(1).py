num = int(input("Введите число n: "))

digit = 3
mult_num = 1

while num > mult_num:
    mult_num *= digit
    if mult_num >= num:
        mult_num //= digit
        break
    digit += 3
print("Произведение натуральных чисел, кратных трём и не превышающим число n: ", mult_num)