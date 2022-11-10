import numpy as np
lst = np.array([1, 2, 3, 4, 5])
print(f'Изначальный список: {lst}')
for i in range(len(lst)-1, 0, -1):
    lst = np.concatenate([lst[:i], np.zeros(3, int), lst[i:]])
print(f'Новый список: {lst}')
