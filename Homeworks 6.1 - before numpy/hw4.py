def reverse_list(lst):
    return lst[::-1]
    

if __name__ == "__main__":
    try:
        x = [int(i) for i in input('Введите числа через запятую: ').split(',')]
        print('Повёрнутый список: {0}'.format(reverse_list(x)))
    except:
        print('Ввод был некорректен')
