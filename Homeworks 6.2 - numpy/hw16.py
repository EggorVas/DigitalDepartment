import numpy as np

def vectMaxBeforZero(vect):
    return max(vect[np.insert((vect==0), 0, False)[:-1:]])

if __name__ == "__main__":
    vect = np.random.randint(0, 5, 15)
    print(f'Сгенерированный вектор:\n{vect}')
    print(f'Максимальное число с нулём перед ним: {vectMaxBeforZero(vect)}')

