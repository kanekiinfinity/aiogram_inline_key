from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mahsulot"),
            KeyboardButton(text="Yordam")
        ],
    ],
    resize_keyboard=True
)