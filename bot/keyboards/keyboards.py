from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

PreExample_keyboard = InlineKeyboardBuilder()
PreExample_keyboard.add(InlineKeyboardButton(text="Action #1", callback_data="first_action"))
PreExample_keyboard.add(InlineKeyboardButton(text="Action #2", callback_data="second_action"))

Example_keyboard = PreExample_keyboard.as_markup()
