from users import models
from typing import Optional, List
from database.schema import BaseModel
from database.validations import unique_valid


class Role(BaseModel):
    name: str
    desc: Optional[str]
    
    class Config:
        orm_mode = True


class User(BaseModel):
    username: str 
    password: str
    is_active: Optional[bool] = False
    role: Optional[Role]

    _rules = [
        
        unique_valid("username", models.User)
    ]

    class Config:
        orm_mode = True   

class RoleUsers(Role):
    users: List[User]

class UserReadOnly(User):
    id: int 
    
class UserRoleId(User):
    role_id: Optional[int] 
