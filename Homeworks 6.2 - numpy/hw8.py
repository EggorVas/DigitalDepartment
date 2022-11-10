import numpy as np

def sum4x4(arr):
    arr_sum = np.empty((4,4), int)
    for i in range(0, 16, 4):
        for j in range(0, 16, 4):
            arr_sum[i//4][j//4] = arr[i:i+4,j:j+4].sum()
    return arr_sum

if __name__ == "__main__":
    lst = np.random.randint(0, 2, (16,16))
    print(f'Сгенерированный массив:\n{lst}')
    print(f'Суммы блоков 4х4:\n{sum4x4(lst)}')
