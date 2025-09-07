from db.models import VacancyDataModel


class VacancyStorageRepositoryBase:
    async def get_object(self, **kwargs) -> VacancyDataModel | None:
        raise NotImplementedError()
