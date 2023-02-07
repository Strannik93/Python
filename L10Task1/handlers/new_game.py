from loader import dp, bot
from aiogram.types import Message
import game
from random import randint as ri
import text

@dp.message_handler(commands=['new_game'])
async def mes_new_game(message: Message):
    if message.from_user.id in game.total:
        if game.total[message.from_user.id][5] == False:
            game.total[message.from_user.id][2] = True
            game.total[message.from_user.id][0] = game.total[message.from_user.id][1]
            toss = ri(False,True)
            if toss == False:
                await message.answer(text.get_candy_text(game.total[message.from_user.id][0],message.from_user.first_name))
            else:
                candy = game.get_candy_bot(game.total[message.from_user.id][0],game.total[message.from_user.id][3])
                game.total[message.from_user.id][0] -= candy
                await message.answer(text.get_candy_bot_text(game.total[message.from_user.id],candy))
                game.total[message.from_user.id][2], win_text = game.check_win(game.total[message.from_user.id],'Бот')
                if win_text != '':
                    await message.answer(win_text)