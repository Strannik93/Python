# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

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
    new_list = []
    if len(my_list)%2 == 1:
        for item in range(int(len(my_list)/2)+1):
            new_list.append(my_list[item]*my_list[len(my_list)-item-1])
    else:
        for item in range(int(len(my_list)/2)):
            new_list.append(my_list[item]*my_list[len(my_list)-item-1])
    print(new_list)
else:
    print('На вводе пустая строка')