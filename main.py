from aiogram import F, Dispatcher, Bot, types

import asyncio
import logging
from apps.handlers import router
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")
