from loader import dp, bot
from aiogram.types import Message
import game
import text

@dp.message_handler(commands=['show_free_pvp'])
async def mes_show_free_pvp(message: Message):
    if message.from_user.id in game.total:
        if game.total[message.from_user.id][4] == 0:
            await message.answer(text.list_pvp_text(game.total_pvp))