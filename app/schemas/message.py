from typing import Optional, List
from core.database.schema import BaseModel
from app.schemas.profile import Profile

class Message(BaseModel):
    text: str 
    to: int

    class Config:
        orm_mode = True


class OwnerProfile(Profile):
    id: int
    avatar: Optional[str]

    class Config:
        orm_mode = True


class Owner(BaseModel):
    id: int
    username: Optional[str]
    profile: Optional[OwnerProfile]

    class Config:
        orm_mode = True

class MessgaeReadOnly(BaseModel):
    id: int 
    text: str
    user: Optional[Owner]

    class Config:
        orm_mode = True

class ChatUsers(BaseModel):
    id: int 
    users: List[Owner]

    class Config:
        orm_mode = True   

class Chat(BaseModel):
    id: int
    users: List[Owner]
    messages: List[MessgaeReadOnly]

    class Config:
        orm_mode = True   