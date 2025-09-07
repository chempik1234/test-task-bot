from typing import Any, Iterable, Coroutine

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.testing import db_spec

from db import Base


class PostgresMixin:
    model = Base

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

    async def get_object(self, **kwargs) -> model | None:
        async with self.session_maker(expire_on_commit=False) as db_session:
            filters = kwargs  # self._field_values(kwargs)

            query_result = await db_session.execute(select(self.model).filter_by(**filters))
            return query_result.scalars().first()

    async def get_objects_field(self, field_name: str) -> list[Any] | None:
        async with self.session_maker(expire_on_commit=False) as db_session:
            result = await db_session.execute(select(getattr(self.model, field_name)))
            return result.scalars().all()
