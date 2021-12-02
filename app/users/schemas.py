from datetime import datetime
from typing import Optional, List
from database.schema import BaseModel
from database.validations import unique_valid

class Role(BaseModel):
    name: str
    desc: Optional[str]

    _rules = [

        unique_valid("name", "app.users.models.Role")
    ]
    
    class Config:
        orm_mode = True

class User(BaseModel):
    username: str 
    password: str
    is_active: Optional[bool] = False
    

    _field_validate = [
        "username",
        "password",
    ]

    _rules = [

        unique_valid("username", "app.users.models.User")
    ]

    class Config:
        orm_mode = True   

class RoleReadOnly(Role):
    id: Optional[int]
    users: List[User]

class UserReadOnly(User):
    id: Optional[int]
    role: Optional[Role]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    last_login: Optional[datetime]
    
class UserRoleId(User):
    role_id: Optional[int] 
