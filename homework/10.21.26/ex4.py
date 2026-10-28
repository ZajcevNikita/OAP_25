numbers = input('Введите числа через пробел: ')
target = int(input('Введите искомое число: '))

def count_occurrences(sequence:int, target:int):
	count = 0

	for i in sequence:
		if i == target:
			count += 1

	return count

def create():
	sequence = []

	for number in numbers.split():
		sequence.append(int(number))

	count = count_occurrences(sequence, target)
	print(f'Число {target} встречается {count} раз(а).')

create()
