import structlog
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot_functions.move_to_menu import move_to_select_channel, move_to_select_surface
from bot_functions.publish import publish_random_vacancy
from exceptions import NoVacancyToPublishException
from init.config.init_config import channels_config
from states import States
from utils import get_logging_extra

logger = structlog.get_logger(name="handlers.menu")

router = Router()


@router.message(States.choose_surface)
async def choose_surface_handler(message: Message, state: FSMContext):
    surface_text = message.text.strip()
    if surface_text not in channels_config.all_surfaces():
        await message.reply("Такой поверхности нет!")
        return

    await move_to_select_channel(state, message.chat.id, surface_text)


@router.message(States.choose_channel)
async def choose_channel_handler(message: Message, state: FSMContext):
    channel_text = message.text.strip()

    logging_extra = get_logging_extra(message.chat.id)

    current_surface = await state.get_value("surface", None)
    if current_surface is None:
        await message.reply("Поверхность не выбрана")
        await move_to_select_surface(state, message.chat.id)
        return

    channel = channels_config.get_channel(surface=current_surface, channel_name=channel_text)

    if channel is None:
        await message.reply("Ошибка! Такой канал не найден, список каналов:\n"
                             f"{'\n'.join(channels_config.channels_in_surface(current_surface))}")
        return

    try:
        await publish_random_vacancy(logging_extra, channel)
        await message.reply("Вакансия опубликована!")
    except NoVacancyToPublishException:
        await message.reply("Не найдено неопубликованных вакансий для этого канала")
        logger.info("didn't publish vacancy by command: no vacancy to publish", extra_data=logging_extra)
    except Exception as e:
        await message.reply(f"Ошибка отправки: {e}", parse_mode=None)
        logger.error("error publishing to chosen channel", exc_info=e, extra_data=logging_extra)
