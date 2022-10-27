from random import randint
x, y = randint(21, 200), randint(0, 21)
print(f' Были сгенерированы два числа: {x} и {y}')
print(f' Результат деления: {x//y} с остатоком {x%y}')
