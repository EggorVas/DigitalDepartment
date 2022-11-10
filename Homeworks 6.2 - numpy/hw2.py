import numpy as np
lst = np.zeros((5,5), int)
for i in range(4):
    lst[i][i+1] = i+1;
print(lst)
