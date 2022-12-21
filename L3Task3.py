# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов, отличной от 0.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def input_spisok():
    while True:
        try:
            x = input('Введите вещественные числа через пробел: ').split()
            my_list = []
            for item in range(len(x)):
                my_list.append(float(x[item]))
            return my_list
        except:
            print('Не введены вещественные числа через пробел')

my_list = input_spisok()
print(my_list)
if len(my_list) > 0:
    min_value = 0
    max_value = 0
    for item in range(len(my_list)):
        if my_list[item]%int(my_list[item]) != 0:
            temp = my_list[item]%int(my_list[item])
            if temp > max_value or max_value == 0:
                max_value = temp
            if temp < min_value or min_value == 0:
                min_value = temp
    if min_value != 0:
        print(f'Разницу между максимальным и минимальным значением дробной части элементов = {round(max_value-min_value, 2)}')
    else: print('На вводе все целые числа')
else:
    print('На вводе пустая строка')