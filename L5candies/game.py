from random import randint as RI

def new_candies():
    while True:
        try:
            candies = int(input('Введите начальное количество конфет: '))
            return candies
        except:
            print('Количество конфет должно быть целым!')

def get_candy(candies: int):
    while True:
        try:
            get_candies = int(input('Сколько хотите забрать конфет: '))
            if 0 < get_candies < 29 and candies > 28:   return get_candies
            elif 0 < get_candies <= candies and candies < 29:   return get_candies
            else:
                if candies < 29: print(f'Можно забрать от 1 до {candies} конфет')
                else: print('Можно забрать от 1 до 28 конфет!')
        except:
            print('Число должно быть целым!')

def new_mode():
    while True:
        try:
            print('1 - PvP, 2 - Игрок против простого бота, 3 - Игрок против сложного бота')
            mode = int(input('Введите число от 1 до 3: '))
            if 0 < mode < 4:    return mode
        except:
            print('Только целое число от 1 до 3!')

def get_candy_bot(candies: int):
    if candies > 28:
        get_candies = RI(1,28)
        print(f'Бот взял {get_candies} конфет.')
        return get_candies
    else:
        get_candies = candies
        print(f'Бот взял {get_candies} конфет.')
        return get_candies

def get_candy_hard_bot(candies: int):
    if candies > 28:
        splitting = candies//28
        if splitting == 3 and candies < 112:
            if candies < 86: temp_1 = 0
            else: temp_1 = 1
            temp_2 = candies - 28*splitting + 26
            get_candies = temp_2-28*(temp_2//28)+temp_1
        elif splitting == 2 and candies < 84:
            if candies < 58: temp_1 = 1
            else: temp_1 = 2
            temp_2 = candies - 28*splitting + 26
            get_candies = temp_2-28*(temp_2//28)+temp_1
        else:
            get_candies = candies - ((splitting)*28+1)
            if get_candies == 0: get_candies = 28
            elif get_candies == -1: get_candies = 27
        print(f'Бот взял {get_candies} конфет.')
        return get_candies
    else:
        get_candies = candies
        print(f'Бот взял {get_candies} конфет.')
        return get_candies