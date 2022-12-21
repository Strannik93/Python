# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101; 3 -> 11; 2 -> 10

def input_value():
    while True:
        try:
            x = input('Введите целое число больше или равно 0: ')
            value = int(x) 
            if value >= 0:
                return value
        except:
            print('Не введено ЦЕЛОЕ число больше или равно 0')

new_value = input_value()
if new_value == 0:
    print(0)
else:
    two_value = []
    while new_value != 0:
        two_value.insert(0, new_value%2)
        new_value //= 2
    print(*two_value, sep='')