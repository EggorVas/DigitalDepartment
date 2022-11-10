import numpy as np

def vectaround1(A):
    global z
    z = np.array([(np.ceil(x) if x>0 else np.floor(x)) for x in A ], int)
    return z

def vectaround2(A):
    global z
    z = np.array([(np.ceil(x) if x>=1 else np.floor(x) if x<=-1 else 0) for x in A ], int)
    return z

if __name__ == "__main__":
    vect = np.random.uniform(-5, 5, 10)
        
    print(f'Сгенерированный вектор:\n{vect}')
    print(f'Округлённый вектор по первому пониманию:{vectaround1(vect)}')
    print(f'Округлённый вектор по второму пониманию:{vectaround2(vect)}')

