from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from init.config import bot_config

publish_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text=bot_config.BOT_PUBLISH_BUTTON_TEXT,
            ),
        ],
    ],
)
