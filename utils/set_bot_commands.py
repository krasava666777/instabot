from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("add", "Добавить аккаунт"),
            types.BotCommand("add_list", "Добавить список аккаунтов"),
            types.BotCommand("get_users", "Вывести список аккаунтов"),
            types.BotCommand("remove", "Удалить аккаунт"),
        ]
    )

