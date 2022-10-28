from functools import reduce
try:
    numbers = [int(x) for x in input(' Перечислите числа через запятую:\n').split(',')]
except:
    print('Результат: что-то не так')
else:
    print(f'Результат: {sorted(numbers, key=lambda x: abs(x))}')
