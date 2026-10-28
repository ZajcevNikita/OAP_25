numbers = input('Введите числа через пробел: ')

def count_zeros(sequence:list[int]):
	count = 0

	for item in sequence:
		if item == 0:
			count += 1

	return count

def create():
	sequence = []

	for number in numbers.split():
		sequence.append(int(number))

	print(f"Количество нулей: {count_zeros(sequence)}")

create()