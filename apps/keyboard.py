from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder
from aiogram import types

def main_menu():
    key = InlineKeyboardBuilder()
    key.row(types.InlineKeyboardButton(text="⏱️ Timing Coach", callback_data="timing"))
    key.row(types.InlineKeyboardButton(text="📈 Tilt Diary", callback_data="tilt"))
    return key.as_markup()

def choice_role():
    key = InlineKeyboardBuilder()
    key.row(types.InlineKeyboardButton(text="[Мид]", callback_data="mid"))
    key.row(types.InlineKeyboardButton(text="[Керри]", callback_data="carry"),(types.InlineKeyboardButton(text="[Хард]", callback_data="hard")))
    key.row(types.InlineKeyboardButton(text="[Саппорт]", callback_data="supp"))
    key.row(types.InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_to_main_menu"))
    return key.as_markup()

def tilt_menu():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="🏆 Победа", callback_data="win"))
    builder.row(types.InlineKeyboardButton(text="💀 Поражение", callback_data="lose"))
    builder.row(types.InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_to_main_menu"))
    return builder.as_markup()

    