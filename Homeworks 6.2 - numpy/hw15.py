import numpy as np

def vectcompare(A, B):
    global z
    z = np.sort(np.unique(A[A in B]))
    return z

if __name__ == "__main__":
    vect1 = np.random.randint(-5, 5, 10)
    vect2 = np.random.randint(-5, 5, 10)
        
    print(f'Сгенерированные векторы:\n{vect1}\n{vect2}')
    print(f'Пересечение:{vectcompare(vect1, vect2)}')

