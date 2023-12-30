from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import course_callback


categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kurslar", callback_data="courses"),
            InlineKeyboardButton(text="Kitoblar", callback_data="books")
        ],
        [
            InlineKeyboardButton(text="Jonibek dev youtube kanaliga o'tish", url="https://www.youtube.com/@jonibek_dev")
        ],
        [
            InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat="")
        ],
        [
            InlineKeyboardButton(text="Ulashish", switch_inline_query="Faoydali bot")
        ]
    ],
    resize_keyboard=True
)


coursesMenu = InlineKeyboardMarkup(row_width=1)
entry = InlineKeyboardButton(text="Entry dasturlash", callback_data=course_callback.new(item_name="entry"))
coursesMenu.insert(entry)
python = InlineKeyboardButton(text="Python dasturlash", callback_data=course_callback.new(item_name="entry"))
coursesMenu.insert(python)