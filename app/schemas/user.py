from datetime import datetime
from typing import Optional, List
from database.schema import BaseModel
from app.schemas.role import RoleReadOnly

class User(BaseModel):
    username: str 
    password: str
    is_active: Optional[bool] = False
    

    class Config:
        orm_mode = True   

class UserReadOnly(User):
    id: Optional[int]
    role: Optional[RoleReadOnly]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    last_login: Optional[datetime]
    
class UserRoleId(User):
    role_id: Optional[int] 
