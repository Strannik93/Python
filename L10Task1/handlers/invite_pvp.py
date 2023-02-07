from loader import dp, bot
from aiogram.types import Message
import game
import text

@dp.message_handler(commands=['invite_pvp'])
async def mes_invite_pvp(message: Message):
    if message.from_user.id in game.total:
        if game.total[message.from_user.id][4] == 0 and len(message.text.split()) == 2:
            if message.text.split()[1].isdigit():
                if message.text.split()[1] in game.total_pvp:
                    if game.total_pvp[message.text.split()[1]][4] == None:
                        game.total[message.from_user.id][4] = message.text.split()[1]
                        game.total_pvp[message.text.split()[1]][3] = message.from_user.id
                        game.total_pvp[message.text.split()[1]][4] = message.from_user.first_name
                        await message.answer(text.game_found)
                        await bot.send_message(game.total_pvp[game.total[message.from_user.id][4]][1], text.invite_alert(game.total_pvp[game.total[message.from_user.id][4]][2],game.total_pvp[game.total[message.from_user.id][4]][4],2))