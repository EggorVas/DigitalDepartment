import re
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonats = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
num = 0
for word in re.split('\W', input(' Введите строку:\n').lower()):
    if len(word) < 2:
        continue
    flag = True
    for i in range(len(word)-1):
        if (word[i] in vowels and word[i+1] in vowels
            or word[i] in consonats and word[i+1] in consonats):
                flag = False
                break
    if flag:
        num += 1    
print(f' Результат: {num}')
