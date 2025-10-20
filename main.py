import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN
from database.db_manager import init_db

from handlers import common, admin, model_selector, tariffs, chat_handler

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    await init_db()

    dp.include_router(admin.router)
    dp.include_router(common.router)
    dp.include_router(model_selector.router)
    dp.include_router(tariffs.router)
    dp.include_router(chat_handler.router) 

    await bot.delete_webhook(drop_pending_updates=True)

    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())