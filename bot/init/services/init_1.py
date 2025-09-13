from db.session import create_sqlalchemy_sessionmaker
from dependency import Dependency
from init.bot import bot
from init.config import channels_config
from init.connections.init_connections import postgres_url, bot_config
from services.sender_service.repositories.telegram import SenderRepositoryTelegram
from services.sender_service.repositories.vk import SenderRepositoryVK
from services.sender_service.service import SenderService
from services.vacancy_service.repositories.storage.postgres import VacancyStorageRepositoryPostgres
from services.vacancy_service.service import VacancyService


def init_postgres_conn():
    return create_sqlalchemy_sessionmaker(
        url=postgres_url,
    )


def init_vacancy_service(vacancy_postgres_conn):
    result = VacancyService(
        storage_repo=VacancyStorageRepositoryPostgres(vacancy_postgres_conn),
    )
    return result


def init_sender_service(bot):
    return SenderService(
        SenderRepositoryTelegram(bot),
        SenderRepositoryVK(channels_config.channels_in_surface("vk"))
    )


postgres_conn = init_postgres_conn()  # Dependency()
vacancy_service = init_vacancy_service(postgres_conn)  # Dependency()

sender_service = init_sender_service(bot)  # Dependency()
