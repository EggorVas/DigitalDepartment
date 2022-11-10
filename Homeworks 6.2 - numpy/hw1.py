import numpy as np
print(np.array([(np.ones(10, int) if i in (0, 9)
                else [1 if j in (0,9) else 0 for j in range(10)])
                for i in range(10)]))
