from loader import dp, bot
from aiogram.types import Message
import game
import text

@dp.message_handler(commands=['set'])
async def mes_set(message: Message):
    if message.from_user.id in game.total:
        if game.total[message.from_user.id][2] == False and len(message.text.split()) == 2 and game.total[message.from_user.id][5] == False:
            if  message.text.split()[1].isdigit():
                count = message.text.split()[1]
                game.total[message.from_user.id][1] = int(count)
                await message.answer(text.get_new_total(game.total[message.from_user.id]))