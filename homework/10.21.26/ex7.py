numbers = input('Введите числа через пробел: ')

def sum_of_abs(sequence:list[int]):
	result = 0

	for item in sequence:
		result += abs(item)

	return result

def create():
	sequence = []

	for number in numbers.split():
		sequence.append(int(number))

	print(f"Сумма модулей чисел: {sum_of_abs(sequence)}")

create()