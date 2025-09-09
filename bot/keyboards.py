from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from init.config import channels_config

surface_markup = ReplyKeyboardMarkup(
    one_time_keyboard=False,
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text=surface,
            )
        ] for surface in channels_config.all_surfaces()
    ]
)

channels_markups = {
    surface: ReplyKeyboardMarkup(
        one_time_keyboard=False,
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(
                    text=channel.name,
                )
            ] for channel in channels_config.channels_in_surface(surface)
        ]
    )
    for surface in channels_config.all_surfaces()
}
