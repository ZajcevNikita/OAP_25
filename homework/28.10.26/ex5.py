import time

number = int(input('Введите количество секунд: '))

for i in range(number, -1, -1):
    print(f"Осталось секунд: {i}")
    time.sleep(1)

print("Пуск")