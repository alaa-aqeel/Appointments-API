from fastapi import APIRouter, Request, Body
from sqlalchemy.sql.elements import or_
from starlette import types
from app.schemas.profile import Employee
from core.resource import resource, BaseResource
from core.depends import Authorize, Profile
from app.repositories.message_respository import MessengerRepository
from app.schemas.message import ChatUsers, Message as MessageSchem
from app.models import Message, User, Chat

router = APIRouter(
            prefix="/messenger",
            dependencies=[Authorize]
        )


@router.get("/user/{id}")
def show_chat_by_user(id: int, request: Request):#{
    """Get all messages by user id"""

    repository = MessengerRepository(request.state.user)
    if request.state.user.id == id:
        repository.abort(424 , {
            "msg": "Woow impressive !!"
        })

        return request.state.user.id == id
    
    user = repository.get_or_failed(User, id)
    chat = repository.chat_with(user).all()
    return chat
#}

@resource(router)
class Messenger(BaseResource):


    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.user = self.request.state.user 
        self.repository = MessengerRepository(self.user)
        
    def index(self): #{ 
        """Get all chat"""

        chats = self.repository.chat_current_user().all()
        return Chat.parse_all(chats, ChatUsers)
    #}

    def show(self, id: int):#{
        """Get all messages by chat id"""

        chats = chats = self.repository.chat_current_user().filter(Chat.id==id).first()
        return chats.parse()
    #}

    def store(self, message: MessageSchem):#{ 
        """Send message"""
        if self.user.id == message.to:
            self.abort(424 , {
                "msg": "Woow impressive !!"
            })
        
        msg = self.repository.create(**message.dict())
        return self.response(msg="Succeefuly send msg", data=msg.parse())
    #} 


@resource(router, "/message")
class Messages(BaseResource):

    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.user = self.request.state.user 
        self.repository = MessengerRepository(self.user)


    def update(self, id: int, text:str=Body(None, embed=True)): # { 
        """Update message"""
        msg = self.repository.update(id, text)
        return self.response(msg=f"Successfuly update msg {id}", data=msg.parse())  
    #}


    def delete(self, id: int): #{ 
        """Delete message"""

        self.repository.delete(id)
        return self.response(msg=f"Successfuly delete msg {id}")       
    #}