from db.models import VacancyDataModel
from services.postgres_mixin import PostgresMixin
from services.vacancy_service.repositories.storage.base import VacancyStorageRepositoryBase


class VacancyStorageRepositoryPostgres(PostgresMixin, VacancyStorageRepositoryBase):
    def __init__(self, sqlalchemy_session_maker):
        super().__init__(sqlalchemy_session_maker, VacancyDataModel)
