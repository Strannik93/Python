from loader import dp, bot
from aiogram.types import Message
import game
import text

@dp.message_handler(commands=['mode'])
async def mes_mode(message: Message):
    if message.from_user.id in game.total:
        if game.total[message.from_user.id][2] == False and game.total[message.from_user.id][5] == False:
            if game.total[message.from_user.id][3] == True:
                game.total[message.from_user.id][3] = False
                await message.answer(text.get_new_mode(game.total[message.from_user.id][3]))
            else:
                game.total[message.from_user.id][3] = True
                await message.answer(text.get_new_mode(game.total[message.from_user.id][3]))