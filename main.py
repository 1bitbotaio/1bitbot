import asyncio
import logging

from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.memory import MemoryStorage

import authentication
import keyboard


TOKEN = "6469970376:AAFk2tdjhir2ooPM0JCEJfLc1xjE1fJOCts"
logging.basicConfig(level=logging.INFO)
storageAuth = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storageAuth)


async def start():
    authentication.register_auth(dp)
    keyboard.register_keyb(dp)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
