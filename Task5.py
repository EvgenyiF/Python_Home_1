# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from random import randint
import math
# Первый вариант решения. Пользователь вводит координаты
x1 = float(input('Введите введите координату: '))
y1 = float(input('Введите введите координату: '))
x2 = float(input('Введите введите координату: '))
y2 = float(input('Введите введите координату: '))

distance = round(math.sqrt((x1 - y1)**2 + (x2-y2)**2) , 3)

print(f'A ({int (x1)}, {int (y1)}), B ({int (x2)}, {int (y2)})')
print (f'Расстояние между точками: {distance}')

# Второй вавриант решения через рандом

# def Get_coordinates(num_plan, left, right):     # координаты точек
#     return tuple([randint(left, right) for i in range(num_plan)])

# def Find_dist(a, b):    # расстояние между точками
#     return round(math.sqrt(sum((x - y)**2 for x, y in zip(a, b))), 3)

# num_plan = 2    # количество осей координат
# left = -5
# right = 5

# point_A = Get_coordinates(num_plan, left, right)
# point_B = Get_coordinates(num_plan,left, right)

# print(f'A {point_A}, B {point_B}')
# print (f'Расстояние между точками: {Find_dist(point_A, point_B)}')