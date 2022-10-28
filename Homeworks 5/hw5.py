num = 0
for x in input('Введите текст: ').split(' '):
    if x.isalpha():
        num += 1
        if num == 3:
            break
    else:
        num = 0
print(f'Есть ли три слова подряд? - {num > 2}')
