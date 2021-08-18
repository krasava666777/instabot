from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command


from loader import dp, db
from states.test import Test, Remove, LS


@dp.message_handler(Command('add'))
async def add_user(message: types.Message, state: FSMContext):
    await message.answer('Введите пользователя')
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def accept_add_user(message: types.Message, state: FSMContext):
    if db.check_user(message.text):
        await message.answer('Такой пользователь уже есть в списке')
    else:
        db.add_user(message.text)
        await message.answer('Добавлен в список')

    await state.reset_state()


@dp.message_handler(Command('remove'))
async def remove_user(message: types.Message, state: FSMContext):
    await message.answer('Введите пользователя для удаления')
    await Remove.res.set()


@dp.message_handler(state=Remove.res)
async def removing(message: types.Message, state: FSMContext):
    if not db.check_user(message.text):
        await message.answer('Такого пользователя не существовало')
    else:
        db.remove_user(message.text)
        await message.answer('Был удален из списка')

    await state.reset_state()


@dp.message_handler(Command('get_users'))
async def get_users(message: types.Message):
    users = []
    for i in db.get_all_users():
        for j in i:
            users.append(j)

    await message.answer(', '.join(users))


@dp.message_handler(Command('add_list'))
async def add_list(message: types.Message, state: FSMContext):
    await message.answer('Введите список пользователей')
    await LS.lt.set()


@dp.message_handler(state=LS.lt)
async def give_list(message: types.Message, state: FSMContext):
    usr = message.text.split('\n')
    for i in usr:
        db.add_user(i)
    await message.answer("Все успешно добавлено")
    await state.reset_state()


