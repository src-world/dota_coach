from aiogram import F, Dispatcher, Bot, types
from config import TOKEN
import asyncio
import logging
from apps.handlers import router

bot = Bot(token=TOKEN)
dp = Dispatcher()


#ROLES_DATA = {
 #   "support": [
  #      {"time": 180, "msg": "🌸 Лотосы!", "repeat": 180},
  #      {"time": 45, "msg": "📦 Пора делать СТАК!", "repeat": 60},
 #       {"time": 405, "msg": "🧠 Руна мудрости через 15 сек!", "repeat": 420},
 #       {"time": 360, "msg": "🥤 Контроль рун 6-й минуты!", "repeat": 0},
 #       {"time": 1200, "msg": "🛡️ Терзатель появился!", "repeat": 0},
 #   ],
 #   "mid":     [
 #       {"time": 360, "msg": "💎 Появилась активная руна!", "repeat": 0},
 #       {"time": 1200, "msg": "🛡️ Терзатель появился!", "repeat": 0},
 #       {"time": 45, "msg": "🫀 Не забываем про рошана!", "repeat": 0},
 #   ],
  #  "carry":   [
  #      {"time": 45, "msg": "📦 Пора делать СТАК!", "repeat": 60},
 #       {"time": 1200, "msg": "🫀 Не забываем про рошана!", "repeat": 0},
 #       {"time": 1200, "msg": "🛡️ Терзатель появился!", "repeat": 0},
 #   ],
 #   "hard":   [
  #      {"time": 1200, "msg": "🫀 Не забываем про рошана!", "repeat": 0},
 #       {"time": 1200, "msg": "🛡️ Терзатель появился!", "repeat": 0},
   # ]
#}




async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")