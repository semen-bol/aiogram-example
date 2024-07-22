import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers import base_commands
from bot.updates import base_updates
from bot.utils.config import config
from bot.database.db import db # Смотрите файл bot/database/db.py !!!!!!!!!!!!!!

from loguru import logger
logger.add("./bot/logs/log_{time}.log", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", compression="zip")

dp = Dispatcher()

@logger.catch
async def main() -> None:
    logger.info("Запуск бота...")
    bot = Bot(token=config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    logger.debug("Бот успешно запущен")

    logger.info("Загрузка роутеров...")
    dp.include_routers(
        base_commands.rt,
        #base_updates.rt смортите файл updates/base_updates.py !!!!!!!!!!
    )
    logger.debug("Роутер [base_commands] загружен")
    #logger.debug("Роутер [base_updates] загружен")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
