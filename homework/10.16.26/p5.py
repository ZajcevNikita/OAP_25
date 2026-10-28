x = float(input('Введите x: '))
y = float(input('Введите y: '))

def describe_point(x:float, y:float):
	if x == 0 and y == 0:
		return 'Точка лежит в начале координат'
	elif x == 0:
		return 'Точка лежит на оси y'
	elif y == 0:
		return 'Точка лежит на оси x'

	if x > 0:
		half = 'первом' if y > 0 else 'четвёртом'
	else:
		half = 'втором' if y > 0 else 'третьем'

	return f'Точка расположена в {half} координатном угле'

def create():
	print(describe_point(x, y))

create()