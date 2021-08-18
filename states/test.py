from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    Q1 = State()


class Remove(StatesGroup):
    res = State()


class LS(StatesGroup):
    lt = State()
