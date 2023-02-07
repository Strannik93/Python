from loader import dp, bot
from aiogram.types import Message
import game
import text

@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    if message.from_user.id in game.total:
        id_game = game.total[message.from_user.id][4]
        print(game.total)
        if game.total[message.from_user.id][5]:
            if game.total_pvp[id_game][5] and game.total_pvp[id_game][1] == message.from_user.id:
                await message.answer(text.get_start_info(game.total[message.from_user.id],message.from_user.first_name,message.from_user.id,game.total_pvp[id_game],'ваш ход'))
            elif game.total_pvp[id_game][5] == False and game.total_pvp[id_game][3] == message.from_user.id:
                await message.answer(text.get_start_info(game.total[message.from_user.id],message.from_user.first_name,message.from_user.id,game.total_pvp[id_game],'ваш ход'))
            else:
                await message.answer(text.get_start_info(game.total[message.from_user.id],message.from_user.first_name,message.from_user.id,game.total_pvp[id_game]))
        else:
            if id_game != 0:
                await message.answer(text.get_start_info(game.total[message.from_user.id],message.from_user.first_name,message.from_user.id,game.total_pvp[id_game]))
            else:
                await message.answer(text.get_start_info(game.total[message.from_user.id],message.from_user.first_name,message.from_user.id))
        pass
    else:
        game.total[message.from_user.id] = [150,150,False,False,0,False]
        await message.answer(text.get_start_info(game.total[message.from_user.id],message.from_user.first_name,message.from_user.id))