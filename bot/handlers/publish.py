import asyncio

import structlog
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot_functions.publish import publish_random_vacancy
from exceptions import NoVacancyToPublishException
from init.config import bot_config
from utils import get_logging_extra

logger = structlog.get_logger(name="handlers.publish")

router = Router()


@router.message(F.text == bot_config.BOT_PUBLISH_BUTTON_TEXT)
async def publish_vacancy_message_handler(message: Message, state: FSMContext):
    logging_extra = get_logging_extra(message.from_user.id)

    logger.info("someone trying to publish vacancy", extra_data=logging_extra)

    try:
        await publish_random_vacancy(logging_extra)
        await message.answer("Вакансия опубликована")
        logger.info("success publish vacancy command", extra_data=logging_extra)
    except NoVacancyToPublishException:
        await message.answer("Не найдено неопубликованных вакансий")
        logger.info("didn't publish vacancy by command: no vacancy to publish", extra_data=logging_extra)
    except Exception as e:
        await message.answer(f"Ошибка отправки вакансии: {e}")
        logger.error("error publishing vacancy by callback", extra_data=logging_extra, exc_info=e)

