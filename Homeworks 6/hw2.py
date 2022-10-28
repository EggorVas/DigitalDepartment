from functools import reduce
try:
    numbers = [float(x) for x in input(' Перечислите числа через запятую:\n').split(',')]
except:
    print('Результат: 0')
else:
    print(f'Результат: {round(max(numbers) - min(numbers), 3)}')
