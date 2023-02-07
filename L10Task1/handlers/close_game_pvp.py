from loader import dp, bot
from aiogram.types import Message
import game
import text

@dp.message_handler(commands=['close_game_pvp'])
async def mes_close_game_pvp(message: Message):
    if message.from_user.id in game.total:  
        if game.total[message.from_user.id][4] != 0:
            id_game = game.total[message.from_user.id][4]
            if game.total[message.from_user.id][5] == True or message.from_user.id == game.total_pvp[id_game][1]:
                await bot.send_message(game.total_pvp[id_game][1], text.close_game_text)
                if game.total_pvp[id_game][4] != None:
                    await bot.send_message(game.total_pvp[id_game][3], text.close_game_text)
                id_first = game.total_pvp[id_game][1]
                game.total[id_first][5] = False
                game.total[id_first][4] = 0
                if game.total_pvp[id_game][4] != None:
                    id_second = game.total_pvp[id_game][3]
                    game.total[id_second][5] = False
                    game.total[id_second][4] = 0
                game.total_pvp.pop(id_game)
            elif message.from_user.id == game.total_pvp[id_game][3]:
                await bot.send_message(game.total_pvp[id_game][1], text.player_exit_text)
                game.total[message.from_user.id][4] = 0
                game.total_pvp[id_game][3] = 'No'
                game.total_pvp[id_game][4] = None