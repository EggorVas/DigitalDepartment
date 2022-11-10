def reverse_odd(lst):
    last_odd_index = len(lst) if len(lst)%2 else len(lst) - 1
    for i in range(1, len(lst) // 2, 2):
        lst[i], lst[last_odd_index+1-i] = lst[last_odd_index+1-i], lst[i]
    return lst

if __name__ == "__main__":
    try:
        lst = [int(i) for i in input('Введите числа через запятую: ').split(',')]
        print(f'Изменённый список: {reverse_odd(lst)}')
    except:
        print('Ввод был некорректен')
