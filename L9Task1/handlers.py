from loader import dp, bot
from aiogram import types
import game
from random import randint as ri

total = {}

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    global total
    if message.from_user.id in total:
        await message.answer(f'Привет, {message.from_user.first_name}!\n'
                        f'На данный момент лимит {total[message.from_user.id][1]} конфет и игра против {game.get_mode(total[message.from_user.id][3])} бота\n'
                        '/new_game - начало игры\n/set - изменить число конфет на значение после пробела\n'
                        '/close_game - завершить игру, /mode - изменение режима игры\n'
                        'Завершить игру можно только при активной игре\n'
                        'Смена режима и числа конфет доступны, когда нет активной игры')
        if total[message.from_user.id][2] == True:
            await message.answer(f'Есть активная игра и осталось {total[message.from_user.id][0]} конфет')
    else:
        temp = []
        temp.append(150)
        temp.append(150)
        temp.append(False)
        temp.append(False)
        total[message.from_user.id] = temp
        await message.answer(f'Привет, {message.from_user.first_name}!\n'
                        f'На данный момент лимит {total[message.from_user.id][1]} конфет и игра против {game.get_mode(total[message.from_user.id][3])} бота\n'
                        '/new_game - начало игры\n/set - изменить число конфет на значение после пробела\n'
                        '/close_game - завершить игру, /mode - изменение режима игры\n'
                        'Завершить игру можно только при активной игре\n'
                        'Смена режима и числа конфет доступны, когда нет активной игры')

@dp.message_handler(commands=['new_game'])
async def mes_new_game(message: types.Message):
    global total
    if message.from_user.id in total:
        total[message.from_user.id][2] = True
        total[message.from_user.id][0] = total[message.from_user.id][1]
        toss = ri(False,True)
        if toss == False:
            await message.answer(f'Ходит {message.from_user.first_name}!\n'
                                f'На столе {total[message.from_user.id][0]} конфет, сколько возьмешь?')
        else:
            candy = game.get_candy_bot(total[message.from_user.id][0],total[message.from_user.id][3])
            total[message.from_user.id][0] -= candy
            await message.answer(f'Ходит бот!\n'
                                f'Бот взял {candy} конфет, на столе осталось {total[message.from_user.id][0]} конфет')
            if total[message.from_user.id][0] == 0:
                await message.answer(f'Победил бот')
                total[message.from_user.id][2] = False

@dp.message_handler(commands=['close_game'])
async def mes_close_game(message: types.Message):
    global total
    if message.from_user.id in total:
        if total[message.from_user.id][2] == True:
            total[message.from_user.id][0] = total[message.from_user.id][1]
            total[message.from_user.id][2] = False
            await message.answer('Игра прервана')

@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total
    if message.from_user.id in total:
        if total[message.from_user.id][2] == False and len(message.text.split()) == 2:
            if  message.text.split()[1].isdigit():
                count = message.text.split()[1]
                total[message.from_user.id][1] = int(count)
                await message.answer(f'Новое количество конфет равно {total[message.from_user.id][1]}')

@dp.message_handler(commands=['mode'])
async def mes_mode(message: types.Message):
    global total
    if message.from_user.id in total:
        if total[message.from_user.id][2] == False:
            if total[message.from_user.id][3] == True:
                total[message.from_user.id][3] = False
                await message.answer('Выбрана игра против простого бота')
            else:
                total[message.from_user.id][3] = True
                await message.answer('Выбрана игра против сложного бота')

@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    if message.from_user.id in total:
        if message.text.isdigit() and total[message.from_user.id][2] == True:
            if total[message.from_user.id][0] < 28:
                if int(message.text) <= total[message.from_user.id][0]:
                    total[message.from_user.id][0] -= int(message.text)
                    await bot.send_message(message.from_user.id, f'Конфет на столе осталось - {total[message.from_user.id][0]}')
                    if total[message.from_user.id][0] == 0:
                        await message.answer(f'Победил {message.from_user.first_name}')
                        total[message.from_user.id][2] = False
                    if total[message.from_user.id][2] == True:
                        candy = game.get_candy_bot(total[message.from_user.id][0],total[message.from_user.id][3])
                        total[message.from_user.id][0] -= candy
                        await message.answer(f'Ходит бот!\n'
                                    f'Бот взял {candy} конфет, на столе осталось {total[message.from_user.id][0]} конфет')
                        if total[message.from_user.id][0] == 0:
                            await message.answer(f'Победил бот')
                            total[message.from_user.id][2] = False
                else:
                    await message.answer(f'В наличии от 1 до {total[message.from_user.id][0]} конфет')
            else:
                if 0 < int(message.text) < 29:
                    total[message.from_user.id][0] -= int(message.text)
                    await bot.send_message(message.from_user.id, f'Конфет на столе осталось - {total[message.from_user.id][0]}')
                    if total[message.from_user.id][0] == 0:
                        await message.answer(f'Победил {message.from_user.first_name}')
                        total[message.from_user.id][2] = False
                    if total[message.from_user.id][2] == True:
                        candy = game.get_candy_bot(total[message.from_user.id][0],total[message.from_user.id][3])
                        total[message.from_user.id][0] -= candy
                        await message.answer(f'Ходит бот!\n'
                                    f'Бот взял {candy} конфет, на столе осталось {total[message.from_user.id][0]} конфет')
                        if total[message.from_user.id][0] == 0:
                            await message.answer(f'Победил бот')
                            total[message.from_user.id][2] = False
                else:
                    await message.answer('Только число от 1 до 28')
        elif total[message.from_user.id][2] == True:
            await message.answer('Только число от 1 до 28')