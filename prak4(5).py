num_a = float(input("Введите координату a: "))
num_b = float(input("Введите координату b: "))
if -1 <= num_a <= 3 and -2 <= num_b <= 4:
    print("Точка находится в заштрихованной области")
else:
    print("Точка НЕ находится в заштрихованной области")
