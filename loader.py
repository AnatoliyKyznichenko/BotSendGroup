from aiogram import Bot, types, Dispatcher, Router, F
from config import config_file
from aiogram.fsm import state

bot = Bot(token=config_file['token'])
dp = Dispatcher(Bot=bot)
