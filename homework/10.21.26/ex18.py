target = int(input('Введите число-признак окончания ввода: '))

def count_until_target(target:int):
	count = 0

	while True:
		number = int(input('Введите число: '))
		if number == target:
			break
		count += 1

	return count

def create():
	count = count_until_target(target)
	print(f"Количество введённых чисел до признака: {count}")

create()