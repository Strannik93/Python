# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов, отличной от 0.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def input_spisok():
    while True:
        try:
            new_string = input('Введите вещественные числа через пробел: ')
            my_list = list(map(float, new_string.split()))
            return my_list
        except:
            print('Не введены вещественные числа через пробел')

my_list = input_spisok()
if len(my_list) == 0: print('На вводе пустая строка')
else:
    my_list = list(filter(lambda x: x%int(x) != 0, my_list))
    if len(my_list) > 0:
        min_value = 0
        max_value = 0
        for item in range(len(my_list)):
            if my_list[item]%int(my_list[item]) > max_value or max_value == 0:
                max_value = my_list[item]%int(my_list[item])
            if my_list[item]%int(my_list[item]) < min_value or min_value == 0:
                min_value = my_list[item]%int(my_list[item])
        if min_value != 0:
            print(f'Разница между максимальным и минимальным значением дробной части элементов = {round(max_value-min_value, 2)}')
    else:
        print('На вводе все целые числа')