# Тест на делимость

for i in range(17):
    number = int(input('Введите число: '))

    if number == 0:
        print('Ошибка: нельзя делить на ноль')
        break

    if (i % number) != 0:
        print(f'{i} не делится на {number}')
    else:
        print(f'{i} делится на {number}')

