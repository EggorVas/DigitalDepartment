import numpy as np

def maxVectInMatrix(matrix):
    norms = np.array([np.linalg.norm(x) for x in matrix])
    indexs = np.where(norms == np.max(norms))[0]
    return indexs, norms[indexs[0]]

if __name__ == "__main__":
    matrix = np.random.randint(0, 5, (5,3))
    print(f'Сгенерированная матрица:\n{matrix}')
    indexs, norm = maxVectInMatrix(matrix)
    print(f'Длина и индкс(ы) самого(ых) длинного(ых) вектора(ов):\n{norm} - {indexs}')

