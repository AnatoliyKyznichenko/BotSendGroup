import asyncio
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from loader import *
import admin_menu
from admin_menu import *
import logging

from config import config_file

logging.basicConfig(filename='main_log.txt')


async def main():
    bot = Bot(token=config_file["token"], parse_mode=ParseMode("HTML"))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(admin_menu.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())