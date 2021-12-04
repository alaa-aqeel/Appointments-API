from enum import Enum
from datetime import datetime, date
from typing import Optional, List
from database.schema import BaseModel

class GenderEnum(str, Enum):
    male = 'male'
    female = 'female'

class Customer(BaseModel):
    fullname: str
    phone: str
    email: Optional[str]
    birthdate: date 
    gender: GenderEnum

    class Config:
        orm_mode = True

class CustomerReadOnly(Customer):
    id: int 
    age: int
    created_at: datetime