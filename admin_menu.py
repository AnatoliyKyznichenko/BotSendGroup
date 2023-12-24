import asyncio

from aiogram import Router, Bot
from aiogram.client import bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, FSInputFile
from config import id_chanel, admin
from aiogram import F
from keyboards_admin import get_admin_menu
from loader import bot

router = Router()


def is_admin(msg):
    return msg.from_user.id == admin


class FormTitle(StatesGroup):
    title = State()
    photo = State()


@router.message(is_admin, Command('admin'))
async def start_admin_menu(msg: Message):
    await msg.answer('Админ меню', reply_markup=get_admin_menu())


@router.message(F.text == '🖥 Добавления')
async def add_title(msg: Message, state: FSMContext):
    await msg.answer('Введите желаемый контент для отправки')
    await state.set_state(FormTitle.title)


@router.message(FormTitle.title)
async def get_title(msg: Message, state: FSMContext):
    await state.update_data(title_text=msg.text)
    await msg.answer('Вставьте фото')
    await state.set_state(FormTitle.photo)


@router.message(FormTitle.photo)
async def get_photo(msg: Message, state: FSMContext):
    # photo_admin = msg.photo[-1].file_id
    # data = await state.get_data()
    # await bot.send_photo(chat_id=id_chanel, text=f'{data.get("title_text", "")}')
    # await bot.send_photo(chat_id=id_chanel, photo=photo_admin)
    # await state.clear()

    photo_admin = msg.photo[-1].file_id
    # Получаем данные из состояния
    data = await state.get_data()
    # Отправляем текст
    await bot.send_message(chat_id=id_chanel, text=f'{data.get("title_text", "")}')
    # Отправляем фото
    await bot.send_photo(chat_id=id_chanel, photo=photo_admin)
    # После отправки данных очищаем состояние
    await state.clear()




