import structlog

from aiogram import Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot_functions.move_to_menu import move_to_select_surface
from states import States
from utils import get_logging_extra

logger = structlog.get_logger(name="commands")

router = Router()


@router.message(Command(commands=["start"]))
async def command_start(message: Message, state: FSMContext):
    logging_extra = get_logging_extra(message.from_user.id)

    authenticated = await state.get_value("authenticated", False)

    if authenticated:
        await move_to_select_surface(state, message.chat.id)
        return

    try:
        logger.info("/start command", extra_data=logging_extra)
        await message.answer("Добро пожаловать! Введите секретный код, чтобы вас пропустили", reply_markup=None)
        await state.set_state(States.login)
    except Exception as e:
        logger.error("error while trying to /start", extra_data=logging_extra, exc_info=e)
