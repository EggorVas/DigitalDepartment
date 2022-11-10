def hello_world():
    print('Привет мир!'[3:8].upper())
    

if __name__ == "__main__":
    try:
        hello_world()
    except:
        print('Ввод был некорректен')
