import numpy as np
def array_sign(lst):
    lst[(abs(lst)>3)*(abs(lst)<8)] = -1*lst[(abs(lst)>3)*(abs(lst)<8)]
    return lst

if __name__ == "__main__":
    try:
        lst = np.array([int(i) for i in input('Введите числа через запятую: ').split(',')])
        print(f'Изменённый список:\t   {array_sign(lst)}')
    except:
        print('Ввод был некорректен')
