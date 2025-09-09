from models.vacancy import Vacancy
from .repositories.storage.base import VacancyStorageRepositoryBase


class VacancyService:
    def __init__(self, storage_repo: VacancyStorageRepositoryBase):
        self.storage_repo = storage_repo

    async def get_object(self, **kwargs) -> Vacancy | None:
        """
        returns first encountered object that satisfies filters or None
        :param kwargs: filters as dict, for example: ``{"field":1,"field__in":[1,2]}``
        :return: first encountered object that satisfies filters or None
        """
        result: Vacancy | None = await self.storage_repo.get_vacancy(**kwargs)
        return result

    async def update_object(self, id: str, **kwargs):
        existing_object = await self.get_object(id=id)

        if not existing_object:
            raise Exception(f"Vacancy with id {id} does not exist")

        await self.storage_repo.update_vacancy(existing_object, **kwargs)
