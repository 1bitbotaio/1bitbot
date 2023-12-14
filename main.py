import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio
from aiogram.filters import Command
import smtplib
from email.mime.text import MIMEText
from database import *

TOKEN = "6469970376:AAFk2tdjhir2ooPM0JCEJfLc1xjE1fJOCts"  # Токен бота
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

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


@dp.message(Command("start"))
async def get_start(message: Message):
    await message.answer("Добро пожаловать в бот Первый.Бит")



# Нажатия на кнопки
async def get_button(message: Message):
    if message.text == "Создать заявку":
        await message.answer("Заявок нет")
    elif message.text == "Обратный звонок":
        await message.answer("Звонка нет")
        await send_email(message.text)
    elif message.text == "Контакты":
        await message.answer('''Линия консультаций: +7 (3812) 332-964 
Круглосуточно omsk@1cbit.ru\n 
г. Омск, ул. Гагарина, д.14, центральный вход, 2 этаж, офис 208, тел. +7 (3812) 320-330
Источник: https://omsk.1cbit.ru/contacts/omsk/omsk/''')
    elif message.text == "FAQ":
        await message.answer("FAQ нет")


# Если есть вернет 1, если нет вернет 0
async def check_user_tg_exists(message: Message):
    user_id = message.from_user.id
    # Проверить наличие пользователя в базе данных
    cursor = connection_clients_db.cursor()
    cursor.execute("SELECT * FROM Clients WHERE TG_ID=?", (user_id,))
    result = cursor.fetchone()
    if result:
        # Пользователь существует в базе данных
        return 1
    else:
        # Пользователя нет в базе данных, добавить его
        return 0


# Передаем сообщение, функция отправляет
async def send_email(message):
    sender = "bit.perw@yandex.ru"
    password = "ojaiaqdykfubxvwi"
    recipient = "cipsevelti@gufum.com"

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    msg = MIMEText(message)
    server.sendmail(sender, recipient, msg.as_string())


# Проверить есть ли инн в базе
@dp.message(F.text.regexp(r'^[\d+]{10,12}$'))
async def check_inn_user_exists(message: Message):
    # Проверить наличие пользователя в базе данных
    cursor = connection_clients_db.cursor()
    cursor.execute("SELECT * FROM Clients WHERE INN=?", (int(message.text),))
    result = cursor.fetchone()
    if result:
        await message.answer("Yes")
        # Пользователь существует в базе данных
        return 1
    else:
        await message.answer("No")
        # Пользователя нет в базе данных
        return 0


async def start():
    dp.message.register(get_button)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
