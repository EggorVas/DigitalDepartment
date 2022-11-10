import numpy as np

def nMaxNumbers(matrix):
    n = int(input('Введите количество наибольших значений: '))
    return sorted(matrix.flatten(), reverse=True)[:(n if n >= 0 else 0)]

if __name__ == "__main__":
    try:
        lst = np.random.randint(0, 10,
                (np.random.randint(2,6),np.random.randint(2,6)))
        print(f'Сгенерированный массив:\n{lst}')
        print(f'Наибольшие числа:\n{nMaxNumbers(lst)}')
    except:
        print('Ввод был некорректен')
