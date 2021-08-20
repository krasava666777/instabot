from aiogram import executor
import asyncio
from handlers.users.insta import insta_bot

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    db.create_table()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(insta_bot(1000))
    executor.start_polling(dp, on_startup=on_startup)
