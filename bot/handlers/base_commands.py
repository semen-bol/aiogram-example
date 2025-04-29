from aiogram import Router, html
from aiogram.types import Message
from aiogram.filters import CommandObject, CommandStart, Command

from loguru import logger

from bot.filters.base import ChatTypeFilter
from bot.keyboards.keyboards import Example_keyboard

rt = Router()

@rt.message(ChatTypeFilter("private"), CommandStart())
async def command_start_handler(message: Message) -> None:
    logger.info(f"Пользователь [{message.chat.first_name}] использовал команду [start]")
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@rt.message(ChatTypeFilter("private"), Command(commands="keyboard"))
async def command_start_handler(message: Message, command: CommandObject) -> None:
    await message.reply("Выберите действие: ", reply_markup=Example_keyboard)
