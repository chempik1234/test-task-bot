from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Vacancy(BaseModel):
    id: str
    company_id: Optional[int]
    external_id: Optional[str]
    link: str
    source: str
    slug: Optional[str]
    name: Optional[str]
    status: Optional[str]
    level: Optional[str]
    description: Optional[str]
    addition: Optional[str]
    work_format: Optional[str]
    location: Optional[str]
    experience: Optional[str]
    position: Optional[str]
    employment: Optional[str]
    salary_from: Optional[int]
    salary_to: Optional[int]
    # raw
    created_at: datetime
    updated_at: Optional[datetime]
    publication_at: Optional[datetime]
