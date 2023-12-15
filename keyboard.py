from aiogram import Dispatcher, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import smtplib
from email.mime.text import MIMEText


cancel_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отмена")]], resize_keyboard=True,
                                      one_time_keyboard=True)


reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Создать заявку"),
        KeyboardButton(text="Обратный звонок")
    ],
    [
        KeyboardButton(text="Контакты"),
        KeyboardButton(text="FAQ")
    ]
], resize_keyboard=True)  # Клавиатура 4 кнопки


async def send_email(message, email_recipient):
    sender = "bit.perw@yandex.ru"
    password = "ojaiaqdykfubxvwi"

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    msg = MIMEText(message)
    server.sendmail(sender, email_recipient, msg.as_string())


class FSMButton1(StatesGroup):
    one = State()


# @dp.message(F.text == "Создать заявку")
async def get_button_1(message: Message, state: FSMContext):
    await state.set_state(FSMButton1.one)
    await message.answer("Введите Ваш вопрос, пожалуйста(одним сообщением)", reply_markup=ReplyKeyboardRemove())
    await message.answer("Если Вы передумали создавать заявку нажмите \"Отмена\"", reply_markup=cancel_keyboard)


# @dp.message(F.text == "Отмена", FSMAuth.one)
async def cancel_handler_1(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer("Создание заявки отменено.",  reply_markup=reply_keyboard)


# @dp.message(F.text, FSMAuth.one)
async def set_question_1(message: Message, state: FSMContext):
    await state.clear()
    await send_email(message.text, "cigali9243@apdiv.com")
    await message.answer("Заявка отправлена", reply_markup=reply_keyboard)


# @dp.message(F.text == "Обратный звонок"")
async def get_button_2(message: Message):
    await send_email(message.text, "cigali9243@apdiv.com")
    await message.answer("Ваш личный менеджер свяжется с Вами в течении 1 часа. Пожалуйста, ожидайте")


async def get_button_3(message: Message):
    await message.answer('''Линия консультаций: +7 (3812) 332-964
Круглосуточно omsk@1cbit.ru\n
г. Омск, ул. Гагарина, д.14, центральный вход, 2 этаж, офис 208, тел. +7 (3812) 320-330
Источник: https://omsk.1cbit.ru/contacts/omsk/omsk/''')


async def get_button_4(message: Message):
    await message.answer('''FAQ никто не придумал, но прототип вот
1. Вопрос 1? - Ответ 1!
2. Вопрос 2? - Ответ 2!
3. Вопрос 3? - Ответ 3!''')


def register_keyb(dp: Dispatcher):
    dp.message.register(get_button_1,  F.text == "Создать заявку")
    dp.message.register(cancel_handler_1, F.text == "Отмена", FSMButton1.one)
    dp.message.register(set_question_1, F.text, FSMButton1.one)
    dp.message.register(get_button_2, F.text == "Обратный звонок")
    dp.message.register(get_button_3, F.text == "Контакты")
    dp.message.register(get_button_4, F.text == "FAQ")
