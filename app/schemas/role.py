from typing import Optional, List
from database.schema import BaseModel

class Role(BaseModel):
    name: str
    desc: Optional[str]

    class Config:
        orm_mode = True

class RoleReadOnly(Role):
    id: Optional[int]
