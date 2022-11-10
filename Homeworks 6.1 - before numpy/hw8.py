def more_than_five(lst):
    return [i for i in lst if abs(i) > 10]

if __name__ == "__main__":
    try:
        lst = [int(i) for i in input('Введите числа через запятую: ').split(',')]
        print(f'Изменённый список: {more_than_five(lst)}')
    except:
        print('Ввод был некорректен')
