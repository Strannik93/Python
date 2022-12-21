# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, 
# стоящих на позиции с нечетным индексом.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def input_spisok():
    while True:
        try:
            x = input('Введите целые числа через пробел: ').split()
            my_list = []
            for item in range(len(x)):
                my_list.append(int(x[item]))
            return my_list
        except:
            print('Не введены ЦЕЛЫЕ числа через пробел')

my_list = input_spisok()
print(my_list)
if len(my_list) > 0:
    rezult = 0
    for item in range(len(my_list)):
        if item%2 == 1:
            rezult += my_list[item]
    print(f'сумму элементов списка, стоящих на позициях с нечетным индексом = {rezult}')
else:
    print('На вводе пустая строка')