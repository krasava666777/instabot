from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/add - Добавить пользователя",
            "/add_list - Добавить список пользователей",
            "/get_users - Вывести список пользователей",
            "/remove - Удалить пользователя")
    
    await message.answer("\n".join(text))
