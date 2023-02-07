from loader import dp, bot
from aiogram.types import Message
import game
import text

@dp.message_handler(commands=['close_game'])
async def mes_close_game(message: Message):
    if message.from_user.id in game.total:
        if game.total[message.from_user.id][2] == True and game.total[message.from_user.id][5] == False:
            game.total[message.from_user.id][0] = game.total[message.from_user.id][1]
            game.total[message.from_user.id][2] = False
            await message.answer(text.close_game_text)