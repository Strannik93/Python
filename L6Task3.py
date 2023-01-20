# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример: - A (3,6); B (2,1) -> 5,09        - A (7,-5); B (1,-1) -> 7,21

import math

def input_value(new_string_1: str, value_1):
    while True:
        try:
            if value_1 == 0: new_string_2 = 'X'
            else: new_string_2 = 'Y'
            value = int(input(f'Введите координаты {new_string_1} точки по оси {new_string_2}: '))
            return value
        except:
            print('Не введено ЦЕЛОЕ число')

point = list(zip([input_value(1,i) for i in range(2)],[input_value(2,i) for i in range(2)]))
distance = math.sqrt((point[0][1]-point[0][0])**2+((point[1][1]-point[1][0])**2))
print(round(distance,2))