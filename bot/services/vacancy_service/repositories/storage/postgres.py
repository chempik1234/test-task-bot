from sqlalchemy import select
from sqlalchemy.orm import selectinload

from db.models import VacancyDataModel, vacancy_postgres_to_model
from models.vacancy import Vacancy
from services.postgres_mixin import PostgresMixin
from services.vacancy_service.repositories.storage.base import VacancyStorageRepositoryBase


class VacancyStorageRepositoryPostgres(PostgresMixin, VacancyStorageRepositoryBase):
    def __init__(self, sqlalchemy_session_maker):
        super().__init__(sqlalchemy_session_maker, VacancyDataModel)

    async def get_vacancy(self, **kwargs) -> Vacancy | None:
        filters_by = kwargs.copy()
        filters = []

        remove_fields = []

        for field, filter_value in filters_by.items():
            if field.endswith("__in") and isinstance(filter_value, list):
                remove_fields.append(field)
                filters.append(getattr(VacancyDataModel, field[: -4]).in_(filter_value))

        for field_to_remove in remove_fields:
            filters_by.pop(field_to_remove)

        result: VacancyDataModel | None = await PostgresMixin.get_object(self, *filters, **filters_by)
        if result is None:
            return None
        return vacancy_postgres_to_model(result)

    async def update_vacancy(self, existing_object: Vacancy, **kwargs) -> Vacancy | None:
        return await self.update_data(existing_object, kwargs)

    def what_to_select(self):
        return select(self.model).options(selectinload(self.model.company))
