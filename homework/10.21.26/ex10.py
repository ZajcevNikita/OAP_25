numbers = input('Введите числа через пробел: ')

def average(sequence:list[int]) -> float:
	result = 0

	for item in sequence:
		result += item

	return result / len(sequence)

def create():
	sequence = []
	
	for number in numbers.split():
		sequence.append(int(number))

	print(f"Среднее арифметическое: {average(sequence)}")

create()