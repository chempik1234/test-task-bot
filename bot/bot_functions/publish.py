import structlog

from exceptions import NoVacancyToPublishException
from init.bot import bot
from init.config import bot_config
from init.services.init_1 import vacancy_service
from init.template import TEMPLATE_TEXT
from models.vacancy import Vacancy
from utils import render

logger = structlog.get_logger("bot_functions.publish")


async def get_vacancy_to_publish() -> Vacancy | None:
    return await vacancy_service.get_object(published=None)


async def publish_random_vacancy(logging_extra):
    vacancy = await get_vacancy_to_publish()

    if vacancy is None:
        raise NoVacancyToPublishException()

    await bot.send_message(
        chat_id=bot_config.BOT_PUBLISH_CHAT_ID,
        text=render(TEMPLATE_TEXT,
                    {
                        "title": vacancy.title,
                        "description": vacancy.description,
                        "company": vacancy.company,
                    }),
    )
    logger.info("published vacancy", extra_data=logging_extra, vacancy_id=vacancy.id)
