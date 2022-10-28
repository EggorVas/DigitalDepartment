from functools import reduce
try:
    numbers = [int(x) for x in input(' Перечислите числа через запятую:\n').split(',')]
except:
    print('Результат: 0')
else:
    print(f'Результат: {reduce(lambda acc, x: acc+x, numbers[::2])*numbers[-1]}')
