from random import randint
from functools import reduce
x = [randint(0, 100) for i in range(3)]

print(f' Были сгенерированы следующие числа: {x}')
print(f' Их произведение: {reduce(lambda acc, n: acc*n, x)}')
