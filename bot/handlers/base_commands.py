from aiogram import Router, html
from aiogram.types import Message, LinkPreviewOptions
from aiogram.filters import CommandObject, CommandStart, Command

from bot.filters.base import ChatTypeFilter
import bot.database.db as db

from loguru import logger

rt = Router()

@rt.message(ChatTypeFilter("private"), CommandStart())
async def command_start_handler(message: Message) -> None:
    logger.info(f"Пользователь [{message.chat.first_name}] использовал команду [start]")
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")