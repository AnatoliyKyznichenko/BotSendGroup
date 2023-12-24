from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder


def get_admin_menu():
    kb = ReplyKeyboardBuilder()
    kb.row(KeyboardButton(text='🖥 Добавления'))
    return kb.as_markup(resize_keyboard=True, row_width=2)