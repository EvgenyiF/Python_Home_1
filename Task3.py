# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

from random import randint
a =int(input('Введите 1 или 2 для выбора метода ввода координат: '))
if a == 1:
    x = float(input('Введите введите координату: '))
    y = float(input('Введите введите координату: '))
else:
    x = randint (-50, 50)
    y = randint (-50, 50)

def get_quarter_number (x, y):
    if x != 0 and y != 0:
        if x * y > 0:
            if x > 0: return 1
            else: return 3
        else:
            if x < 0: return 2
            else: return 4
    else: 
        if x == 0: return 'OY'
        else: return 'OX'
    
print (f'x = {x}, y = {y} -> {get_quarter_number(x, y)}')