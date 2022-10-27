height = int(input(' Введите высоту: '))
width = height * 3
print(f' Тогда ширина будет: {width}')
print('\n Макет ковра:')

if height % 2 == 1:
    for separators in range(1, height, 2):
        print(('.|.' * separators).center(width, '-'))

    print('WELCOME'.center(width, '-'))

    for separators in range(height-2, 0, -2):
        print(('.|.' * separators).center(width, '-'))
else:
    for separators in range(1, height, 2):
        print((('.|.' * (separators//2))+'.||.'+('.|.' * (separators//2))).center(width, '-'))

    print('WELLCOME'.center(width, '-'))

    for separators in range(height-2, 0, -2):
        print((('.|.' * (separators//2))+'.||.'+('.|.' * (separators//2))).center(width, '-'))
