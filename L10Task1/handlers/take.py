from loader import dp, bot
from aiogram.types import Message
import game
import text

@dp.message_handler()
async def mes_all(message: Message):
    if message.from_user.id in game.total:
        if game.total[message.from_user.id][5]:
            id_game = game.total[message.from_user.id][4]
            if game.total_pvp[id_game][5] and game.total_pvp[id_game][1] == message.from_user.id:
                step = True
            elif game.total_pvp[id_game][5] == False and game.total_pvp[id_game][3] == message.from_user.id:
                step = True
            else:
                step = False
            if message.text.isdigit():
                if step:
                    check, new_text = game.check_candy(game.total_pvp[id_game],message.text,True)
                    if check:
                        game.total_pvp[id_game][0] -= int(message.text)
                        await bot.send_message(game.total_pvp[id_game][1], new_text)
                        await bot.send_message(game.total_pvp[id_game][3], new_text)
                        check_win, win_text = game.check_win(game.total_pvp[id_game],message.from_user.first_name)
                        if check_win == False:
                            await bot.send_message(game.total_pvp[id_game][1], win_text)
                            await bot.send_message(game.total_pvp[id_game][3], win_text)
                            id_first = game.total_pvp[id_game][1]
                            game.total[id_first][5] = False
                            game.total[id_first][4] = 0
                            id_second = game.total_pvp[id_game][3]
                            game.total[id_second][5] = False
                            game.total[id_second][4] = 0
                            game.total_pvp.pop(id_game)
                        else:
                            if game.total_pvp[id_game][5]:
                                 game.total_pvp[id_game][5] = False
                            else:
                                game.total_pvp[id_game][5] = True
                    else:
                        await message.answer(new_text)
            elif step:
                await message.answer(text.error_1_28)
        else:
            if message.text.isdigit() and game.total[message.from_user.id][2] == True:
                check, new_text = game.check_candy(game.total[message.from_user.id],message.text)
                if check:
                    game.total[message.from_user.id][0] -= int(message.text)
                    await bot.send_message(message.from_user.id, new_text)
                    game.total[message.from_user.id][2], win_text = game.check_win(game.total[message.from_user.id],message.from_user.first_name)
                    if win_text != '':
                        await message.answer(win_text)
                    if game.total[message.from_user.id][2] == True:
                        candy = game.get_candy_bot(game.total[message.from_user.id][0],game.total[message.from_user.id][3])
                        game.total[message.from_user.id][0] -= candy
                        await message.answer(text.get_candy_bot_text(game.total[message.from_user.id],candy))
                        game.total[message.from_user.id][2], win_text = game.check_win(game.total[message.from_user.id],'Бот')
                        if win_text != '':
                            await message.answer(win_text)
                else:
                    await message.answer(new_text)
            elif game.total[message.from_user.id][2] == True:
                await message.answer(text.error_1_28)