from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder
from aiogram import types
from steam_parser import get_top_deals


def subscribe():
    key = InlineKeyboardBuilder()
    key.row(types.InlineKeyboardButton(text="Узнать сегодняшний топ🔝", callback_data="subscribe"))
    return key.as_markup()

