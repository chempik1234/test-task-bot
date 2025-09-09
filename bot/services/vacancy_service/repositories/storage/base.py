from db.models import VacancyDataModel
from models.vacancy import Vacancy


class VacancyStorageRepositoryBase:
    async def get_vacancy(self, **kwargs) -> Vacancy | None:
        raise NotImplementedError()

    async def update_vacancy(self, existing_object: Vacancy, **kwargs) -> Vacancy | None:
        raise NotImplementedError()
