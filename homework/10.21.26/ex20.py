numbers = input('Введите натуральные числа через пробел: ')
digit = int(input('Введите искомую цифру: '))

def count_ending_with_digit(sequence:list[int], digit:int):
	count = 0

	for item in sequence:
		if item % 10 == digit:
			count += 1

	return count

def create():
	sequence = []

	for number in numbers.split():
		sequence.append(int(number))

	count = count_ending_with_digit(sequence, digit)
	print(f"Количество чисел, оканчивающихся на {digit}: {count}")

create()