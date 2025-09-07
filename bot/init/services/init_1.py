from db.session import create_sqlalchemy_sessionmaker
from init.connections.init_connections import postgres_url, bot_config
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

postgres_conn = init_postgres_conn()  # Dependency()
vacancy_service = init_vacancy_service(postgres_conn)  # Dependency()
