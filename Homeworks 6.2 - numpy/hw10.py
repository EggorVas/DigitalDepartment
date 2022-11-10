import numpy as np

def noneEquel(arr):
    noneEquelArrays = []
    for i in arr:
        for j in i[1:]:
            if i[0] != j:
                noneEquelArrays.append(i)
                break
    return np.array(noneEquelArrays)

if __name__ == "__main__":
    lst = np.random.randint(1, 3, (10,3))
    print(f'Сгенерированный массив:\n{lst}')
    print(f'Строки с неравными значениями:\n{noneEquel(lst)}')
