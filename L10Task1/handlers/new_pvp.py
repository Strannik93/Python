from loader import dp, bot
from aiogram.types import Message
import game
from random import randint as ri
import text

@dp.message_handler(commands=['new_pvp'])
async def mes_new_pvp(message: Message):
    if message.from_user.id in game.total:
        if game.total[message.from_user.id][4] == 0:
            new_key, check = 1, True
            while check:
                if new_key not in game.total_pvp:
                    check = False
                else:
                    new_key += 1
            game.total_pvp[new_key] = [game.total[message.from_user.id][1],message.from_user.id,message.from_user.first_name,'No',None,ri(False,True)]
            game.total[message.from_user.id][4] = new_key
            await message.answer(text.create_pvp_text(new_key))