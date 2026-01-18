from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def main_manu():
    key = InlineKeyboardBuilder()
    key.row(types.InlineKeyboardButton(text="⏱️ Timing Coach", callback_data="timing"))
    key.row(types.InlineKeyboardButton(text="🎯 Draft Sniper", callback_data="draft"))
    key.row(types.InlineKeyboardButton(text="📈 Tilt Diary", callback_data="tilt"))
    return key.as_markup()

def choice_role():
    key = InlineKeyboardBuilder()
    key.row(types.InlineKeyboardButton(text="[Мид]", callback_data="mid"))
    key.row(types.InlineKeyboardButton(text="[Саппорт]", callback_data="supp"))
    key.row(types.InlineKeyboardButton(text="[Керри]", callback_data="carry"))
    key.row(types.InlineKeyboardButton(text="[Хард]", callback_data="hard"))
    return key.as_markup()