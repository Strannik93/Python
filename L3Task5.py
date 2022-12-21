# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def input_value():
    while True:
        try:
            x = input('Введите целое число больше или равно 0: ')
            value = int(x) 
            if value >= 0:
                return value
        except:
            print('Не введено ЦЕЛОЕ число больше или равно 0')

def fibonacci(count_max, my_list, count = 0):
    if count <= count_max > 0:
        if count == 0:
            my_list.append(0)
            return fibonacci(count_max, my_list, count+1)
        elif count == 1:
            my_list.append(1)
            my_list.insert(0,1)
            return fibonacci(count_max, my_list, count+1)
        else:
            my_list.append(my_list[len(my_list)-1]+my_list[len(my_list)-2])
            my_list.insert(0, ((abs(my_list[1])+abs(my_list[0]))*((-1)**(count-1))))
            return fibonacci(count_max, my_list, count+1)
    else:
        return

new_value = input_value()
my_list = []
fibonacci(new_value, my_list)
print(*my_list, sep=' ')