def input_spisok():
    while True:
        try:
            new_string = input('Введите целые числа через пробел: ')
            my_list = list(map(int, new_string.split()))
            return my_list
        except:
            print('Не введены ЦЕЛЫЕ числа через пробел')

my_list = input_spisok()
print(my_list)
if len(my_list) > 0:
    rezult = 0
    for i, item in enumerate(my_list):
        if i%2 == 1:
            rezult += item
    print(f'сумму элементов списка, стоящих на позициях с нечетным индексом = {rezult}')
else:
    print('На вводе пустая строка')