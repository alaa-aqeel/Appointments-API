from datetime import datetime
from enum import IntEnum, Enum
from typing import Optional, List
from core.database.schema import BaseModel

class Role(BaseModel):
    id: int 
    name: str
    desc: Optional[str]

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str
    
    class Config:
        orm_mode = True  

class RoleEnum(IntEnum, Enum):
    customer = 1
    employee = 2
 
class AuthUser(User):
    password: str
    role: Optional[RoleEnum] = 1

    class Config:
        orm_mode = True 

class AdminUser(User):
    role: Optional[int] = 1
    password: str
    is_active: Optional[bool] = False

class UserProfile(User):
    password: str
     
class UserReadOnly(User):
    id: Optional[int]
    role: Optional[Role]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    last_login: Optional[datetime]
    is_active: Optional[bool] = False