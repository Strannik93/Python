# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

from random import randint as r

my_list = []
for i in range(10):
    my_list.append(r(0,100))
print(my_list)
for i in range(len(my_list)-1):
    random_position = r(i+1,len(my_list)-1)
    temp = my_list[random_position]
    my_list[random_position] = my_list[i]
    my_list[i] = temp
print(my_list)