from aiogram import F, Dispatcher, Bot
from config import TOKEN
import asyncio
from aiogram.filters import CommandStart
from aiogram.types import Message
import logging

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!") 

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")