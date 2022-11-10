def season(month):
    global s
    if month < 3:
        s = "Зима"
    elif month < 6:
        s = "Весна"
    elif month < 9:
        s = "Лето"
    elif month < 12:
        s = "Осень"
    else:
        s = "Зима"

if __name__ == "__main__":
    try:
        season(int(input('Введите номер месяца: ')))
        print('Это {0}'.format(s))
    except:
        print('Ввод был некорректен')
