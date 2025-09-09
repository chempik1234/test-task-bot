from typing import Any, Iterable

from pydantic import BaseModel
from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError

from db import Base


class PostgresMixin:
    model = Base.__class__

    def __init__(self, sqlalchemy_session_maker, model):
        self.session_maker = sqlalchemy_session_maker
        self.model = model

    def _model_attrs_from_dict(self, data_object, data_dict) -> None:
        for key, value in data_dict.items():
            if value is not None and hasattr(data_object, key):
                setattr(data_object, key, value)

    async def get_objects(self, *filters, **filters_by) -> Iterable[model]:
        async with self.session_maker(expire_on_commit=False) as db_session:
            result = await db_session.execute(select(self.model).filter(*filters).filter_by(**filters_by))
            return result.scalars().all()

    async def get_object(self, *filters, **filter_by) -> model | None:
        async with self.session_maker(expire_on_commit=False) as db_session:

            query_result = await db_session.execute(select(self.model).filter_by(**filter_by).filter(*filters))
            return query_result.scalars().first()

    async def get_objects_field(self, field_name: str) -> list[Any] | None:
        async with self.session_maker(expire_on_commit=False) as db_session:
            result = await db_session.execute(select(getattr(self.model, field_name)))
            return result.scalars().all()

    async def update_data(self, existing_object, data_dict) -> None:
        async with self.session_maker(expire_on_commit=False) as db_session:
            try:
                # data_dict = self._field_values(data_dict)
                # if isinstance(existing_object, BaseModel):
                #     existing_object = self.model(**existing_object.model_dump())

                # self._model_attrs_from_dict(existing_object, data_dict)
                statement = update(self.model).values(**data_dict).where(self.model.id == existing_object.id)
                # db_session.add(existing_object)
                await db_session.execute(statement)
                await db_session.commit()
            except IntegrityError:
                await db_session.rollback()
