from loader import dp, bot
from aiogram.types import Message
import game
import text

@dp.message_handler(commands=['reply_invite_pvp'])
async def mes_reply_invite_pvp(message: Message):
    if message.from_user.id in game.total:
        if game.total[message.from_user.id][5] == False and game.total[message.from_user.id][4] != 0:
            if len(message.text.split()) == 2:
                if game.total_pvp[game.total[message.from_user.id][4]][4] != None and message.from_user.id == game.total_pvp[game.total[message.from_user.id][4]][1]:
                    id_game = game.total[message.from_user.id][4]
                    if message.text.split()[1].lower() == 'yes':
                        game.total[game.total_pvp[id_game][1]][5] = True
                        game.total[game.total_pvp[id_game][3]][5] = True
                        await message.answer(text.answer_yes)
                        await bot.send_message(game.total_pvp[id_game][3], text.invite_alert(game.total_pvp[id_game][2],game.total_pvp[id_game][4],1))
                    elif message.text.split()[1].lower() == 'no':
                        await message.answer(text.answer_no)
                        await bot.send_message(game.total_pvp[id_game][3], text.invite_alert(game.total_pvp[id_game][2],game.total_pvp[id_game][4],0))
                        game.total[game.total_pvp[id_game][3]][4] = 0
                        game.total_pvp[id_game][3] = 'No'
                        game.total_pvp[id_game][4] = None