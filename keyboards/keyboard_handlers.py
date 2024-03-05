from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

addStaff_kb = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Add staff"),
    ]],
    resize_keyboard=True
)