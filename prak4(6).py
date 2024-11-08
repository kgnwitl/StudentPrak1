num_a = float(input("Введите координату a (x): "))
num_b = float(input("Введите координату b (y): "))

if (-2 <= num_a <= 0 and -3 <= num_b <= 2 and ((round(2.5, 1) * num_a) + 2) >= num_b)\
    or (0 <= num_a <= 2 and -3 <= num_b <= 2 and ((round(-2.5, 1) * num_a) + 2) >= num_b):
        print("Принадлежит")
else:
    print("Не принадлежит")
