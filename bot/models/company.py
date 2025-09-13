from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Company(BaseModel):
    id: int
    name: str
    full_name: Optional[str]
    inn: Optional[str]
    description: Optional[str]
    rate: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    rate_at: Optional[datetime]
    deleted_at: Optional[datetime]
    account_id: Optional[int]
