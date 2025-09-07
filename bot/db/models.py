from sqlalchemy import Column, Integer, String, Text, DateTime
from .base import Base


class VacancyDataModel(Base):
    __tablename__ = "Vacs"

    id = Column(
        Integer,
        primary_key=True,
        name="Id",
    )
    published = Column(
        DateTime,
        nullable=True,
        name="Published",
    )
    company = Column(
        String(50),
        nullable=False,
        name="Company",
    )
    description = Column(
        Text,
        nullable=False,
        name="Description",
    )
    title = Column(
        String(50),
        nullable=False,
        name="Title",
    )

    def __repr__(self):
        return f"<Vacs(title='{self.title}', company='{self.company}')>"
