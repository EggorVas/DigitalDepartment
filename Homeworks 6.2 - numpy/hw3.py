import numpy as np
lst = np.array(np.random.randint(0, 10,
            (np.random.randint(2, 6), np.random.randint(2, 6))), float)
print(f'Сгенерированная матрица:\n{lst}')
mean = lst.mean(axis=1)
print(f'Cреднее с каждой строки:\n{mean}')
for i in range(len(mean)):
    for j in range(len(lst[0])):
        lst[i][j] = lst[i][j] - mean[i]
print(f'Вычтено среднее с каждой строки:\n{lst}')
