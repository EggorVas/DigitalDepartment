import numpy as np

def replace_rows(matrix, num1, num2):
    matrix[num1], matrix[num2] = matrix[num2].copy(), matrix[num1].copy()
    return matrix

if __name__ == "__main__":
    try:
        lst = np.random.randint(0, 10,
            (np.random.randint(2, 6), np.random.randint(2, 6)))
        print(f'Сгенерированная матрица:\n{lst}')
        nums = [int(i)%len(lst) for i in input('Введите через запятую индексы строк: ').split(',')]
        print(f'Изменённыя матрица:\n{replace_rows(lst, nums[0], nums[1])}')
    except:
        print('Ввод был некорректен')
