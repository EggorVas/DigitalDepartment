import numpy as np

def vectcos(vect1, vect2):
    return (vect1@vect2) / ((vect1**2).sum()*(vect2**2).sum())**0.5

if __name__ == "__main__":
    vect1 = np.random.randint(0, 5, 3)
    vect2 = np.random.randint(0, 5, 3)
        
    print(f'Сгенерированные вектора:\n{vect1}\n{vect2}')
    print(f'Косинус угла между векторами:{vectcos(vect1, vect2)}')
