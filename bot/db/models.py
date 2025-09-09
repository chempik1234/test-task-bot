from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import JSONB

from models.vacancy import Vacancy
from .base import Base


class VacancyDataModel(Base):
    __tablename__ = "vacancies_crawled"

    id = Column(String, nullable=False, primary_key=True)
    company_id = Column(Integer, nullable=True)
    external_id = Column(String, nullable=True)
    link = Column(String, nullable=False)
    source = Column(String, nullable=False)
    slug = Column(String, nullable=True)
    name = Column(String, nullable=True)
    status = Column(String, nullable=True)
    level = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    addition = Column(Text, nullable=True)
    work_format = Column(String, nullable=True)
    location = Column(String, nullable=True)
    experience = Column(String, nullable=True)
    position = Column(String, nullable=True)
    employment = Column(String, nullable=True)
    salary_from = Column(Integer, nullable=True)
    salary_to = Column(Integer, nullable=True)
    raw = Column(JSONB, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
    publication_at = Column(DateTime, nullable=True)


def vacancy_postgres_to_model(data_model: VacancyDataModel) -> Vacancy:
    return Vacancy(
        id=data_model.id,
        company_id=data_model.company_id,
        external_id=data_model.external_id,
        link=data_model.link,
        source=data_model.source,
        slug=data_model.slug,
        name=data_model.name,
        status=data_model.status,
        level=data_model.level,
        description=data_model.description,
        addition=data_model.addition,
        work_format=data_model.work_format,
        location=data_model.location,
        experience=data_model.experience,
        position=data_model.position,
        employment=data_model.employment,
        salary_from=data_model.salary_from,
        salary_to=data_model.salary_to,
        created_at=data_model.created_at,
        updated_at=data_model.updated_at,
        publication_at=data_model.publication_at,
    )
