import numpy as np

def mode(arr):
    unq = np.unique(arr)
    numbers = np.array([len(arr[arr == i]) for i in unq])
    number = max(numbers)
    mode = np.array(list(unq))[numbers == number]
    return mode, number

if __name__ == "__main__":
    lst = np.random.randint(1, 10, np.random.randint(5, 15))
    print(f'Сгенерированный массив:\n{lst}')
    mode, number = mode(lst)
    print(f'Массив с модами:{mode}\nЧастота встречаемости:{number}')

