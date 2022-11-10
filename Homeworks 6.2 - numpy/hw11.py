import numpy as np

def diffrows(matrix):
    return np.unique(matrix, axis=0)

if __name__ == "__main__":
    lst = np.random.randint(0, 2,
                (np.random.randint(5,10),3))
    print(f'Сгенерированный массив:\n{lst}')
    print(f'Разные строки в массиве:\n{diffrows(lst)}')

