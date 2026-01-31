from aiogram.filters import CommandStart, Command
from aiogram import F, types
from aiogram.types import Message, CallbackQuery
from aiogram import Router
import apps.keyboard as kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from steam_parser import get_top_deals
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton, InlineKeyboardMarkup
router = Router()
from main import bot
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(
        "Привет! Я бот, который будет присылать тебе топ-10 игр со скидкой в Steam! "
        "\n\nЧтобы получить первый топ нажми кнопку ниже", reply_markup=kb.subscribe())
    
@router.callback_query(F.data == "subscribe")
async def subscribe(callback: CallbackQuery):
    deals = get_top_deals(limit=10)
    for deal in deals:
        rmessage = f"{deal.get("game_ul")}\n\n🎮 - Название : {deal.get("name")}\n\n🎁 - Скидка : {deal.get("skidka")}\n\n💸 - Обычная цена : {deal.get("start_price")}\n\n💸 - Текущая цена : {deal.get("exit_prive")}\n"
        await callback.message.answer(rmessage)
    await callback.message.answer(
    "Нажми кнопку чтоб получить сегодняшний топ!", reply_markup=kb.subscribe())
