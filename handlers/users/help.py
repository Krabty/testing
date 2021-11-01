from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


# @dp.message_handler(CommandHelp())
@dp.message_handler(commands="help")
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/weather - Вывести погоду"
            )
    
    await message.answer("\n".join(text))
