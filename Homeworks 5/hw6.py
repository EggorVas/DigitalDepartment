strings = [x.strip().replace('right', 'left') for x in input(' Введите строки через запятые:\n').split(',') ]
print(f' Результат:\n{",".join(strings)}')
