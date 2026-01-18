from aiogram import F, Dispatcher, Bot
from config import TOKEN
import asyncio
import logging

bot = Bot(token=TOKEN)
dp = Dispatcher()

ROLES_DATA = {
    "support": [
        {"time": 180, "msg": "🌸 Лотосы!", "repeat": 180},
        {"time": 45, "msg": "📦 Пора делать СТАК!", "repeat": 60},
        {"time": 405, "msg": "🧠 Руна мудрости через 15 сек!", "repeat": 420},
        {"time": 1200, "msg": "🛡️ Терзатель появился!", "repeat": 0},
    ],
    "mid": [
        {"time": 120, "msg": "🥤 Активная руна в миду!", "repeat": 120},
        {"time": 360, "msg": "🥤 Контроль рун 6-й минуты!", "repeat": 0},
        {"time": 405, "msg": "🧠 Руна мудрости!", "repeat": 420},
    ]
}

async def play_timing_coach(bot, chat_id, role):
    seconds = 0
    events = ROLES_DATA.get(role, [])
    
    try:
        while seconds < 3600: 
            await asyncio.sleep(1)
            seconds += 1
            for event in events:
                if event['repeat'] > 0:
                    if seconds >= event['time'] and (seconds - event['time']) % event['repeat'] == 0:
                        await bot.send_message(chat_id, f"<b>{event['msg']}</b>", parse_mode="HTML")
                else:
                    if seconds == event['time']:
                        await bot.send_message(chat_id, f"<b>{event['msg']}</b>", parse_mode="HTML")
    except asyncio.CancelledError:
        pass

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")