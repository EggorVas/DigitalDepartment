def allseven():
    lst = [i for i in range(0, 500, 7) if '8' in str(i) ]
    return lst

if __name__ == "__main__":
    print(f'Числа, делящиеся на 7 и содержащие 8: {allseven()}')
