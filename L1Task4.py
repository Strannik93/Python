# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

fourth = int(input('Введите номер четверти плоскости координат: '))
if fourth == 1:
    print('по оси X > 0, по оси Y > 0')
elif fourth == 2:
    print('по оси X < 0, по оси Y > 0')
elif fourth == 3:
    print('по оси X < 0, по оси Y < 0')
elif fourth == 4:
    print('по оси X > 0, по оси Y < 0')
else:
    print('Четверти с таким номером не существует')