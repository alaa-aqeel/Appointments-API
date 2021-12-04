from datetime import datetime
from typing import Optional, List
from database.schema import BaseModel

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

class AuthUser(User):
    password: str

    class Config:
        orm_mode = True 

class AdminUser(User):
    role_id: Optional[int] 
    password: str
    is_active: Optional[bool] = False

class UserProfile(User):
    pass 

class UserReadOnly(User):
    id: Optional[int]
    role: Optional[Role]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    last_login: Optional[datetime]
    is_active: Optional[bool] = False