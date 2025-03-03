import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers import base_commands
from bot.updates import base_updates
from bot.utils.config import config
from bot.database.db import db # Смотрите файл bot/database/db.py и файл test.py
from bot.middlewares.ultrabase_middleware import CommandFlood

from loguru import logger
logger.add("./bot/logs/log_{time}.log", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", compression="zip")

db = db(host="localhost:27017", # host:port
        username=None, # root
        password=None, # qwerty123
        database="example", # users / example / chats
        isLocal=True # база данных локальна? boolean
        )

dp = Dispatcher()

@logger.catch
async def main() -> None:
    # Bot
    logger.info("Запуск бота..."); bot = Bot(token=config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML)); logger.debug("Бот успешно запущен")
    # Мидлварь
    dp.message.middleware(CommandFlood()) # можно указать и больше время и меньше, но по моим замерам 4 - самое оптимальное )
    # Database
    logger.info("Подключаю базу данных..."); ping = await db.ping()
    if ping == True: logger.debug("База данных подключена")
    else: logger.debug("База данных не смогла ответить на запрос")
    # Routes
    logger.info("Загрузка роутеров..."); dp.include_routers(
        base_commands.rt,
        base_updates.rt
    )
    logger.debug("Роутер [base_commands] загружен")
    logger.debug("Роутер [base_updates] загружен")

    await dp.start_polling(bot,
                           allowed_updates=["message", "inline_query", "chat_member", "my_chat_member"])


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt: logger.debug("Exiting...")
