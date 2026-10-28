numbers = input('Введите числа через пробел: ')
digit = int(input('Введите искомую цифру: '))

def sum_ending_with_digit(sequence:list[int], digit:int):
	result = 0

	for item in sequence:
		if item % 10 == digit:
			result += item

	return result

def create():
	sequence = []

	for number in numbers.split():
		sequence.append(int(number))

	total = sum_ending_with_digit(sequence, digit)
	print(f"Сумма чисел, оканчивающихся на {digit}: {total}")

create()