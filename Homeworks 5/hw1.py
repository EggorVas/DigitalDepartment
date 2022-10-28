x = int(input(' Введите число, пожалуйста: '))
result = (('Fizz' if x % 3 == 0 else '') + ' ' + ('Buzz' if x % 5 == 0 else '')).strip()
print(' Результат: ' + str(result if result != '' else x))
