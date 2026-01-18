from aiogram.filters import CommandStart, Command
from aiogram import F, types
from aiogram.types import Message, CallbackQuery
from aiogram import Router
import apps.keyboard as kb
from main import Bot, play_timing_coach
import asyncio
router = Router()

active_timers = {}

@router.callback_query(F.data.startswith("start_"))
async def start_coach(callback: types.CallbackQuery, bot: Bot):
    role = callback.data.split("_")[1]
    user_id = callback.from_user.id

    if user_id in active_timers:
        active_timers[user_id].cancel()
        
    task = asyncio.create_task(play_timing_coach(bot, callback.message.chat.id, role))
    active_timers[user_id] = task
    
    await callback.answer("Таймер запущен! Удачи в катке!", show_alert=True)
