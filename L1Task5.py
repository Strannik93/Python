# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример: - A (3,6); B (2,1) -> 5,09        - A (7,-5); B (1,-1) -> 7,21

import math
point1 = []
point2 = []
point1.append(int(input('Введите координаты 1 точки по оси X: ')))
point1.append(int(input('Введите координаты 1 точки по оси Y: ')))
point2.append(int(input('Введите координаты 2 точки по оси X: ')))
point2.append(int(input('Введите координаты 2 точки по оси Y: ')))
distance = math.sqrt((point2[0]-point1[0])**2+((point2[1]-point1[1])**2))
print(round(distance,2))