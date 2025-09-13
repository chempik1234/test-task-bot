from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from models.company import Company
from ..base import Base


class CompanyDataModel(Base):
    __tablename__ = 'companies'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    inn = Column(String, nullable=True)
    description = Column(String, nullable=True)
    rate = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
    rate_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    account_id = Column(Integer, nullable=True)


def company_postgres_to_model(data_model: CompanyDataModel) -> Company:
    return Company(
        id=data_model.id,
        name=data_model.name,
        full_name=data_model.full_name,
        inn=data_model.inn,
        description=data_model.description,
        rate=data_model.rate,
        created_at=data_model.created_at,
        updated_at=data_model.updated_at,
        rate_at=data_model.rate_at,
        deleted_at=data_model.deleted_at,
        account_id=data_model.account_id
    )