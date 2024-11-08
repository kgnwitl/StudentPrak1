#import math

num_a = float(input("Введите координату a: "))
num_b = float(input("Введите координату b: "))
#evk_dist = math.sqrt(pow(num_a, 2) +  pow(num_b, 2))
if -1 <= num_a <= 3 and -2 <= num_b <= 4:
    print("Точка находится в заштрихованной области")
else:
    print("Точка НЕ находится в заштрихованной области")

#print(f"Евклидово расстояние точки от центра: {evk_dist}")