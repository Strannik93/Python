close_game_text = 'Игра прервана'
player_exit_text = '2 игрок отозвал предложение сыграть'
error_1_28 = 'Только число от 1 до 28'
game_found = 'Свободная игра найдена\nЖдите ответа от создавшего игру'
answer_no = 'В созданной вами игре снова свободно место 2 игрока'
answer_yes = 'Начнется пвп игра'

def error_1_max(lim):
    return f'Только число от 1 до {lim}'

def get_new_mode(mode: bool):
    return f'Выбрана игра против {get_mode(mode)} бота'

def get_new_total(total_id):
    return f'Новое количество конфет равно {total_id[1]}'

def get_mode(mode):
    if mode == False: return 'простого'
    else: return 'сложного'

def get_start_info(total_id, first_name, player, total_pvp = None, step = None):
    text = ''
    text += f'Привет, {first_name}!\n'
    if total_id[5] == False:
        text += f'На данный момент лимит {total_id[1]} конфет и игра против {get_mode(total_id[3])} бота\n'
        text += '/new_game - начало игры\n/set - изменить число конфет на значение после пробела\n'
        text += '/close_game - завершить игру, /mode - изменение режима игры\n'
        text += '\nЗавершить игру можно только при активной игре\n'
        text += 'Смена режима и числа конфет доступны, когда нет активной игры\n'
        if total_id[4] == 0:
            text += '\n/new_pvp - создать пвп игру с вашим лимитом конфет\n/show_free_pvp - показать свободные пвп игры\n'
            text += '/invite_pvp - предложить сыграть открывшему пвп игру (добавить через пробел id игры)\n'
        else:
            if player == total_pvp[1]:
                text += f'\nСоздана пвп игра с лимитом {total_pvp[0]} конфет и id игры {total_id[4]}\n'
                if total_pvp[4] != None:
                    text += f'{total_pvp[4]} ожидает от вас ответа на предложение сыграть\n'
                    text += '/reply_invite_pvp - ответ на приглашение (добавить через пробел yes или no)\n'
                else:
                    text += 'На данный момент нет желающего сыграть в пвп игру, ждите или завершите игру\n'
                text += '/close_game_pvp - завершить игру\n'
            elif player == total_pvp[3]:
                text += f'\nВы ожидаете ответа от {total_pvp[2]}\n'
                text += f'В игре с количеством конфет {total_pvp[0]} и id игры {total_id[4]}\n'
                text += '/close_game_pvp - отозвать приглашение\n'
        if total_id[2]:
            text += f'\nЕсть активная игра и осталось {total_id[0]} конфет'
    else:
        text += '/close_game_pvp - завершить игру\n'
        if step != None:
            text += f'\nЕсть активная пвп игра: осталось {total_pvp[0]} конфет и {step}'
        else:
            text += f'\nЕсть активная пвп игра: осталось {total_pvp[0]} конфет'
    return text

def get_candy_text(total, first_name):
    return f'Ходит {first_name}!\nНа столе {total} конфет, сколько возьмешь?'

def get_candy_bot_text(total_id, candy):
    return f'Ходит бот!\nБот взял {candy} конфет, на столе осталось {total_id[0]} конфет'

def check_win_text(first_name):
    return f'Победил {first_name}'

def surplus_text(total):
    return f'Осталось {total} конфет'

def surplus_pvp_text(total,name1,name2,candy,toss: bool):
    if toss:
        return f'{name1} (1 игрок) взял {candy} конфет\nОсталось {total} конфет'
    else:
        return f'{name2} (2 игрок) взял {candy} конфет\nОсталось {total} конфет'

def list_pvp_text(total_pvp: dict):
    text = ''
    for key in total_pvp:
        if total_pvp[key][3] == 'No':
            text += f'{key}: создана {total_pvp[key][2]} c лимитом {total_pvp[key][0]}\n'
    if text == '':
        return 'Свободных игр нет'
    else:
        return text

def create_pvp_text(item):
    return f'Игра создана успешно с id {item}'

def invite_alert(name1, name2, flag: int):
    if flag == 2:
        return f'Здравствуйте {name1}, к вашей игре добавился {name2}\nОжидается ответ'
    elif flag == 1:
        return f'Здравствуйте {name2}, {name1} согласился сыграть в игру'
    elif flag == 0:
        return f'Здравствуйте {name2}, {name1} отказался сыграть в игру'