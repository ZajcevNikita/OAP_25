numbers = input('Введите числа через пробел: ')
sequence = [int(i) for i in numbers.split()]

product = 1

for i in sequence:
    if i == 0:
        continue

    product *= i

print(product)