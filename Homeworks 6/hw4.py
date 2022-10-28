from functools import reduce
try:
    numbers = sorted([int(x) for x in input(' Перечислите числа через запятую:\n').split(',')])
except:
    print('Результат: что-то не так')
else:
    length = len(numbers)
    print('Результат: {0}'.format(numbers[length//2] if length%2==1 else (numbers[length//2-1]+numbers[length//2])/2))
