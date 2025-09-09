import asyncio

import structlog
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot_functions.move_to_menu import move_to_select_surface
from bot_functions.publish import publish_random_vacancy
from exceptions import NoVacancyToPublishException
from init.config import bot_config
from states import States
from utils import get_logging_extra

logger = structlog.get_logger(name="handlers.login")

router = Router()


@router.message(States.login)
async def publish_vacancy_message_handler(message: Message, state: FSMContext):
    logging_extra = get_logging_extra(message.from_user.id)

    logger.info("someone trying to log in", extra_data=logging_extra)

    user_input = message.text
    if user_input == bot_config.BOT_SECRET_KEY_ON_LOGIN:
        await state.update_data(authenticated=True)
        await move_to_select_surface(state, message.chat.id)
        return

    logger.warn("someone failed to log in", extra_data=logging_extra, user_input=user_input)

    await message.answer("Код неверный!")

    await state.clear()
