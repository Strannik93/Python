import game
from random import randint as RI

def main_menu(mode=False):
    print('введите: start - начать игру, mode - режим игры, exit - выход')
    if mode == False: print('Текущий режим - 2 игрока.')
    else: print('Текущий режим - против бота.')
    command = input('Введите команду: ')
    if command == 'start': new_game(mode)
    elif command == 'mode': 
        mode = new_mode(mode)
        main_menu(mode)
    elif command == 'exit': exit()
    else: main_menu(mode)

def new_mode(mode):
    if mode == False: mode = True
    else: mode = False

def exit():
    print('завершение программы')

def new_game(mode):
    matrix = game.create_matrix()
    game.print_matrix(matrix)
    toss = RI(False, True)
    if toss == True:
        first = 'X'
        second = 'O'
    else:
        first = 'O'
        second = 'X'
    if mode == False: 
        first_player = '1 игрок'
        second_player = '2 игрок'
    else:
        first_player = '1 игрок'
        second_player = 'Бот'
    print(f'{first_player} ставит {first}, {second_player} ставит {second}')
    steps = True
    while steps == True:
        if toss == True:
            print(f'Ходит {first_player}({first}):')
            line, row = game.step(matrix)
            matrix[line][row] = first
            game.print_matrix(matrix)
            toss = False
            steps = game.check_steps(matrix,first,first_player)
        else:
            if mode == False:
                print(f'Ходит {second_player}({second}):')
                line, row = game.step(matrix)
                matrix[line][row] = second
                game.print_matrix(matrix)
                toss = True
                steps = game.check_steps(matrix,second,second_player)
            else:
                print(f'Ходит {second_player}({second}):')
                line, row = game.bot_step(matrix,second)
                matrix[line][row] = second
                game.print_matrix(matrix)
                toss = True
                steps = game.check_steps(matrix,second,second_player)
    exit()

main_menu()