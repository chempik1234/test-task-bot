from typing import Any

from db.models import VacancyDataModel
from models.vacancy import Vacancy
from .repositories.storage.base import VacancyStorageRepositoryBase


class VacancyService:
    def __init__(self, storage_repo: VacancyStorageRepositoryBase):
        self.storage_repo = storage_repo

    def _to_model(self, result: VacancyDataModel) -> Vacancy:
        return Vacancy(
            description=result.description,
            company=result.company,
            title=result.title,
            id=result.id,
            published=result.published,
        )

    async def _get_object(self, **kwargs) -> VacancyDataModel | None:
        result: VacancyDataModel | None = await self.storage_repo.get_object(**kwargs)
        return result

    async def get_object(self, **kwargs) -> Vacancy | None:
        result: VacancyDataModel | None = await self._get_object(**kwargs)
        if not result:
            return None
        return self._to_model(result)
