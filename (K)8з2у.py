a = int(input("Введите вариант:"))
x = float(input("Введите Х:"))
y = float(input("Введите Y:"))


if a == 1:
    if (x**2 + y**2 <= 25) and (0 <= y <= 5):
        print("Красный цвет")
    elif (-2 <= x <= 2) and (-7 <= y <= 0):
        print("Цвет желтый")
    elif (-5 <= x <= 5) and (-8 <= y <= -7):
        print("Цвет зеленый")
    else:
        print("Мимо")
        
        
if a == 2:
    if x**2 + y**2 <= 1:
        print("Красный цвет")
    elif (x**2 + y**2 >= 1) and (x**2 + y**2 <= 9):
        print("Цвет оранжевый")
    elif ((4 <= x <= 7) and (-1 <= y <= 1)) or ((-1 <= x <= 1) and (4 <= y <= 7)) or ((-4 <= x <= -7) and (-1 <= y <= 1)) or ((-1 <= x <= 1) and (-7 <= y <= -4)):
        print("Цвет желтый")
    else:
        print("Мимо")
    
    
if a == 3:
    if x**2 + y**2 <= 1:
        print("Цвет желтый")
    elif x**2 + (y-3)**2 <= 1:
        print("Красный цвет")
    elif x**2 + (y+3)**2 <= 1:
        print("Цвет зеленый")
    elif ((-2 <= x <= 2) and (-5 <= y <= 5)) or ((-3 <= x <= 3) and (5 <= y <= 6)):
        print("Цвет серый")
    else:
        print("Мимо")
        
        
if a == 4:
    if (x+3)**2 + y**2 <= 1:
       print("Красный цвет")
    elif (x-3)**2 + y**2 <=1:
        print("Цвет желтый")
    elif x**2 + (y-3)**2 <=1:
        print("Цвет розовый")
    elif x**2 + (y+3)**2 <=1:
        print("Цвет зеленый")
    elif x**2 + y**2 <=1:
        print("Цвет синий")
    elif x**2 + y**2 <=25:
        print("Цвет серый")
    else:
        print("Мимо")


if a == 5:
    if (x**2 + (y-2)**2 <= 25) and (2 <= y <= 7):
       print("Цвет голубой")
    elif ((x-1)**2 + (y+4)**2 <= 2.25) and ((x-1)**2 + (y+4)**2 >= 0.25):
        print("Красный цвет")
    elif (-0.5 <= x <= 0.5) and (-4 <= y <= 2):
        print("Цвет серый")
    else:
        print("Мимо")
  

if a == 6:
    if ((x+3)**2 + (y-3)**2 <=16) and ((x-3)**2 + (y-3)**2 >=16) and ((x)**2 + (y+2)**2 >= 16):
        print("Цвет желтый")
    elif ((x+3)**2 + (y-3)**2 >=16) and ((x-3)**2 + (y-3)**2 >=16) and ((x)**2 + (y+2)**2 <= 16):
        print("Цвет голубой")
    elif ((x+3)**2 + (y-3)**2 >=16) and ((x-3)**2 + (y-3)**2 <=16) and ((x)**2 + (y+2)**2 >= 16):
        print("Цвет фиолетовый")
    elif ((x+3)**2 + (y-3)**2 <=16) and ((x-3)**2 + (y-3)**2 <=16) and (x**2 + (y+2)**2 <= 16):
        print("Желтый + голубой + фиолетовый")
    
    elif ((x+3)**2 + (y-3)**2 <=16) and ((x-3)**2 + (y-3)**2 <=16) and ((x)**2 + (y+2)**2 >= 16):
        print("Цвет желтый + фиолетовый")
    elif ((x+3)**2 + (y-3)**2 >=16) and ((x-3)**2 + (y-3)**2 <=16) and ((x)**2 + (y+2)**2 <= 16):
        print("Цвет голубой + фиолетовый")
    elif ((x+3)**2 + (y-3)**2 <=16) and ((x-3)**2 + (y-3)**2 >=16) and ((x)**2 + (y+2)**2 <= 16):
        print("Цвет желтый + голубой")    
    
    else:
        print("Мимо")
        

if a == 7:
    if (4 <= x <= 5) and (4 <= y <= 7):
        print("Цвет зеленый")
    elif ((-4 <= x <= -2) and (1 <= y <= 3)) or ((2 <= x <= 4) and (1 <= y <= 3)):
        print("Цвет желтый")
    elif ((x+3)**2 + (y+1)**2 <= 1) or ((x-3)**2 + (y+1)**2 <= 1):
        print("Цвет серый")
    elif (-6 <= x <= 6) and (-1 <= y <= 4):
        print("Цвет голубой")
    else:
        print("Мимо")
        

if a == 8:
    if ((x+3)**2 + (y-2)**2 <= 1) or ((x-3)**2 + (y-2)**2 <= 1):
        print("Цвет синий")
    elif (x**2 + (y+2)**2 <= 4) and (-4 <= y <= -2):
        print("Красный цвет")
    elif x**2 + y**2 <= 36:
        print("Цвет желтый")
    else:
        print("Мимо")
        

if a == 9:
    if (-5 <= x <= 5) and (-2 <= y <= -1):
        print("Цвет фиолетовый")
    elif (-4 <= x <= 4) and (-1 <= y <= 0):
        print("Цвет синий")
    elif (-3 <= x <= 3) and (0 <= y <= 1):
        print("Цвет голубой")
    elif (-2 <= x <= 2) and (1 <= y <= 2):
        print("Цвет зеленый")
    elif (-1 <= x <= 1) and (2 <= y <= 3):
        print("Цвет желтый")
    elif (x-3)**2 + (y-6)**2 <= 1:
        print("Красный цвет")
    else:
        print("Мимо")


if a == 10:
    if (x**2 + (y-4)**2 <= 64) and (-4 <= y <= 0):
        print("Цвет коричневый")
    elif (0 <= x <= 1) and (0 <= y <= 8):
        print("Цвет серый")
    elif ((x+2)**2 + (y-4)**2 <= 16) and ((x-2)**2 + (y-4)**2 >= 16):
        print("Цвет красный")
    else:
        print("Мимо")
        
        
if a == 11:
    if ((x-2)**2 + (y-7)**2 <= 1) and ((x-3)**2 + (y-7)**2 >= 1):
        print("Цвет желтый")
    elif ((x+1.5)**2 + (y-5.5)**2 <= 6.25) or ((-6 <= x <= 6) and (-5 <= y <= -1)):
        print("Цвет зеленый")
    elif (-2 <= x <= -1) and (-1 <= y <= 3):
        print("Цвет коричневый")
    elif (-6 <= x <= 6) and (-1 <= y <= 9):
        print("Цвет голубой")
    else:
        print("Мимо")
       
        
if a == 12:    
    if (x**2 + y**2 <= 16) and (x**2 + y**2 >= 9) or (-2 <= x <=2 and -1 <= y <=1):
        print("Красный цвет")
    elif (-8 <= y <= -4) and (-1 <= x <=1):
        print("Цвет серый")
    else:
        print("Мимо")