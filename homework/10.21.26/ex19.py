numbers = input('Введите числа через пробел: ')

def is_ascending(sequence:list[int]):
	for i in range(len(sequence) - 1):
		if sequence[i] >= sequence[i + 1]:
			return False

	return True

def create():
	sequence = []

	for number in numbers.split():
		sequence.append(int(number))

	print(is_ascending(sequence))

create()