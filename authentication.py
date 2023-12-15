from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import types, F, Dispatcher

from database import *
from keyboard import reply_keyboard


def check_user_tg_exists(message: types.Message):
    user_id = message.from_user.id
    # Проверить наличие пользователя в базе данных
    cursor = connection_clients_db.cursor()
    cursor.execute("SELECT * FROM Clients WHERE TG_ID=?", (user_id,))
    result = cursor.fetchone()
    if result:
        # Пользователь существует в базе данных
        return 1
    else:
        # Пользователя нет в базе данных
        return 0


class FSMAuth(StatesGroup):
    begin = State()


# @dp.message(Command("start"))
async def command_start(message: types.Message, state: FSMContext):
    await state.set_state(FSMAuth.begin)
    await message.answer("Добро пожаловать в бот Первый.Бит")
    if check_user_tg_exists(message) == 1:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.clear()
        await message.answer("Спасибо, что Вы с нами!", reply_markup=reply_keyboard)
    else:
        await message.answer("Введите Ваш ИНН, пожалуйста(только цифры)")


# @dp.message(F.text.regexp(r'^[\d+]{10,12}$'), FSMAuth.begin)
async def check_inn_user_exists(message: types.Message, state: FSMContext):
    # Проверить наличие пользователя в базе данных
    cursor = connection_clients_db.cursor()
    cursor.execute("SELECT * FROM Clients WHERE INN=?", (int(message.text),))
    result = cursor.fetchone()
    if result:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.clear()
        await message.answer("Спасибо, что Вы с нами!", reply_markup=reply_keyboard)
        # Пользователь существует в базе данных
    else:
        await message.answer("ИНН неверный, проверьте правильность ввода, либо обратитесь в поддержку")
        # Пользователя нет в базе данных


# @dp.message(F.text, FSMAuth.begin)
async def text_validation(message: types.Message):
    await message.reply("Еблан! Написано же введи ИНН!!!")


def register_auth(dp: Dispatcher):
    dp.message.register(command_start, Command("start"))
    dp.message.register(check_inn_user_exists, F.text.regexp(r'^[\d+]{10,12}$'), FSMAuth.begin)
    dp.message.register(text_validation, F.text, FSMAuth.begin)
