checkUp = False
thickness = 5 # Если запущен в системе, где exit() не работает
try:
    thickness = int(input('Please, write the thickness in the drawing: '))
except:
    checkUp = True
if (checkUp or thickness < 1):
    print('This is not a natural number! I won\'t talk to you! :_p')
    exit()
c = str(input('And write the symbol: '))[0]

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i)) # Здесь не нужен ljust, т.к. справа ничего нет

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
