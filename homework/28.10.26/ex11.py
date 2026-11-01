# Сумма ряда

amount = int(input('Введите количество чисел: '))

result = 0

for i in range(amount):
    number = int(input('Введите число: '))
    result += number if i % 2 == 0 else -number

print(result)