def distance(x1, y1, x2, y2):
    return ((x[0]-x[2])**2+(x[1]-x[3])**2)**0.5

if __name__ == "__main__":
    try:
        x = [int(i) for i in input('Введите x1, y1, x2, y2 через запятую: ').split(',')]
        print(f' Расстояние: {distance(x[0], x[1], x[2], x[3])}')
    except:
        print('Ввод был некорретным')     
