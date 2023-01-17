import game
from random import randint as RI

def main_menu(candies: int, mode = 1):
    print('введите: start - начать игру, candies - смена начального количества конфет, mode - выбор режима, exit - выход')
    print(f'На данный момент {candies} конфет.')
    if mode == 1: print('Режим: игрок против игрока')
    elif mode == 2: print('Режим: игрок против простого бота')
    elif mode == 3: print('Режим: игрок против сложного бота')
    command = input('Введите команду: ')
    if command == 'start': new_game(candies, mode)
    elif command == 'candies': 
        candies = game.new_candies()
        main_menu(candies, mode)
    elif command == 'mode':
        mode = game.new_mode()
        main_menu(candies, mode)
    elif command == 'exit': exit()
    else: main_menu(candies, mode)

def new_game(candies: int, mode: int):
    toss = RI(False, True)
    while candies > 0:
        if toss == False:
            print(f'Ходит 1 игрок. На данный момент конфет {candies}')
            candies -= game.get_candy(candies)
            if candies == 0:    print('Победа 1 игрока')
            toss = True
        else:
            if mode == 1:
                print(f'Ходит 2 игрок. На данный момент конфет {candies}')
                candies -= game.get_candy(candies)
                if candies == 0:    print('Победа 2 игрока')
                toss = False
            elif mode == 2:
                print(f'Ходит бот. На данный момент конфет {candies}')
                candies -= game.get_candy_bot(candies)
                if candies == 0:    print('Победил бот')
                toss = False
            elif mode == 3:
                print(f'Ходит бот. На данный момент конфет {candies}')
                candies -= game.get_candy_hard_bot(candies)
                if candies == 0:    print('Победил бот')
                toss = False
    exit()

def exit():
    print('завершение программы')

main_menu(150)