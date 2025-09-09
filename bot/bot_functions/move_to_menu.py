import structlog
from aiogram.fsm.context import FSMContext

from bot_functions.publish import get_vacancy_message_text
from init.bot import bot
from keyboards import surface_markup, channels_markups
from states import States

logger = structlog.get_logger(name="bot_functions.move_to")


async def move_to_select_surface(state: FSMContext, chat_id: int | str):
    await state.set_state(States.choose_surface)
    await bot.send_message(chat_id=chat_id, text="Выберите поверхность", reply_markup=surface_markup)


async def move_to_select_channel(state: FSMContext, chat_id: int | str, surface: str):
    await state.set_state(States.choose_channel)
    await bot.send_message(chat_id=chat_id, text="Выберите канал", reply_markup=channels_markups[surface])
    await state.update_data(surface=surface)
