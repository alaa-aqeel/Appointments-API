from enum import Enum
from datetime import datetime, date
from typing import Optional, List
from app.models import category
from core.database.schema import BaseModel
from app.schemas.category import CategoryReadOnly


class GenderEnum(str, Enum):
    male = 'male'
    female = 'female'


class Profile(BaseModel):
    fullname: str
    phone: str
    email: Optional[str]
    gender: GenderEnum

    class Config:
        orm_mode = True

class Customer(Profile):
    birthdate: date 


class Employee(Profile):
    about: Optional[str] 
    special: str
    address: Optional[str] 
    price: Optional[int]
    category: str

class CustomerReadOnly(Customer):
    id: int 
    age: Optional[int]
    created_at: Optional[datetime]

class EmployeeReadOnly(Employee):
    id: int 
    avatar: Optional[str]
    created_at: Optional[datetime]
    category: Optional[CategoryReadOnly]