from datetime import datetime

import structlog

from config.channel_config import Channel
from exceptions import NoVacancyToPublishException
from init.services.init_1 import vacancy_service, sender_service
from init.template import VACANCY_TEMPLATE
from models.vacancy import Vacancy
from utils import get_logging_extra

logger = structlog.get_logger("bot_functions.publish")


async def get_vacancy_to_publish(channel: Channel) -> Vacancy | None:
    return await vacancy_service.get_object(published=None, **channel.rules_as_kwargs())


def get_vacancy_message_text(vacancy: Vacancy) -> str:
    return VACANCY_TEMPLATE.render(vacancy=vacancy)


async def publish_random_vacancy(logging_extra, channel: Channel):
    if logging_extra is None:
        logging_extra = get_logging_extra()

    vacancy = await get_vacancy_to_publish(channel)

    if vacancy is None:
        raise NoVacancyToPublishException()

    try:
        text = get_vacancy_message_text(vacancy=vacancy)

        await sender_service.send(channel, text)

        await vacancy_service.update_object(vacancy.id, published=datetime.now().replace(tzinfo=None))
        logger.info("published vacancy", extra_data=logging_extra, vacancy_id=vacancy.id)

    except Exception as e:
        logger.exception("error publishing vacancy", extra_data=logging_extra)
        raise e
