# Дзета-функция Римана

amount = int(input('Введите натуральное число: '))

pi = 3.141592653589793
theta_sum = 0.0

for i in range(1, amount + 1):
    theta_sum += 1.0 / (i * i)

result = (pi * pi) / theta_sum
print(f"{result:.15f}")