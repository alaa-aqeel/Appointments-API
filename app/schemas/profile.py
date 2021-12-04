from enum import Enum
from datetime import datetime, date
from typing import Optional, List
from database.schema import BaseModel

class GenderEnum(str, Enum):
    male = 'male'
    female = 'female'

class Profile(BaseModel):
    fullname: str
    phone: str
    email: Optional[str]
    gender: GenderEnum

class Customer(Profile):
    birthdate: date 


class Employee(Profile):
    about: str 
    special: str
    address: str
    price: str

    class Config:
        orm_mode = True

class CustomerReadOnly(Customer):
    id: int 
    age: int
    created_at: datetime

class EmployeeReadOnly(Employee):
    id: int 
    avatar: str 
    created_at: datetime