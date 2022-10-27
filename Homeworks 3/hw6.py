number = input(' Введите число: ')
result = 1;
for char in number:
    if (char.isdigit() and int(char) > 0):
        result *= int(char)
print(f' Перемноженные цифры числа: {result}')
