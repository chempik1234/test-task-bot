import structlog

from aiogram import Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import publish_keyboard
from utils import get_logging_extra

logger = structlog.get_logger(name="commands")

router = Router()


@router.message(Command(commands=["start"]))
async def command_start(message: Message, state: FSMContext):
    logging_extra = get_logging_extra(message.from_user.id)
    try:
        logger.info("/start command", extra_data=logging_extra)
        await message.answer("Добро пожаловать!", reply_markup=publish_keyboard)
    except Exception as e:
        logger.error("error while trying to /start", extra_data=logging_extra, exc_info=e)
