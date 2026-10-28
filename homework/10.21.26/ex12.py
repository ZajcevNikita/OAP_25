numbers = input('Введите числа через пробел: ')

def product_of_abs(sequence:list[int]):
	result = 1

	for item in sequence:
		result *= abs(item)

	return result

def create():
	sequence = []
	
	for number in numbers.split():
		sequence.append(int(number))

	print(f"Произведение модулей элементов: {product_of_abs(sequence)}")

create()