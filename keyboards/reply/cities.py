from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


cities = ReplyKeyboardMarkup(

    keyboard=[

        [
            KeyboardButton("Toshkent"),
            KeyboardButton("Samarqand")
        ],
        [
            KeyboardButton("Namangan"),
            KeyboardButton("Jizzax")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,

)