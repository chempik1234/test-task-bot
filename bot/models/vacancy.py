from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Vacancy(BaseModel):
    id: int
    published: Optional[datetime]
    company: str
    description: str
    title: str
