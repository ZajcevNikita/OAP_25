# Шварценеггер против Годзиллы

import math

div_amount = int(input('Введите количество дробинок: '))

num_sum = 0
den_sum = 1

for i in range(div_amount):
    numerator = int(input('Введите числитель урона от дробинки: '))
    denominator = int(input('Введите знаменатель урона от дробинки: '))

    num_sum = num_sum * denominator + numerator * den_sum
    den_sum = den_sum * denominator

    g = math.gcd(num_sum, den_sum)

    num_sum //= g
    den_sum //= g

    print(f"Упрощённая дробь: {num_sum}/{den_sum}")