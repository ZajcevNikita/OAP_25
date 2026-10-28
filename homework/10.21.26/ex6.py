numbers = input('Введите числа через пробел: ')

def product(sequence:list[int]):
	result = 1

	for item in sequence:
		result *= item

	return result

def create():
	sequence = []

	for number in numbers.split():
		sequence.append(int(number))
	
	print(f'Произведение чисел: {product(sequence)}')

create()