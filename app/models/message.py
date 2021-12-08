from sqlalchemy import Table
from sqlalchemy.sql.expression import null
from core.database.model import Model, TimeStamp, Column, types, ForeignKey, relationship
from app.schemas.message import MessgaeReadOnly, Chat


chats_users = Table('chats_users', Model.metadata,
    Column("chat_id",types.Integer, ForeignKey('chat.id')),
    Column("user_id",types.Integer, ForeignKey('user.id'))
)

class Chat(Model, TimeStamp):
    
    __schema__ = Chat

    title = Column(types.String(45), nullable=True)
    users = relationship("User",
        secondary="chats_users",
        back_populates="chats")

class Message(Model, TimeStamp):

    __schema__ = MessgaeReadOnly

    text = Column(types.Text, nullable=False)  
    is_readable = Column(types.Boolean, default=0) 

     # One User To Many messanges as recive 
    chat_id = Column(types.Integer, ForeignKey('chat.id'))
    chat = relationship('Chat',backref="messages",
                    foreign_keys="Message.chat_id")

    # One User To Many messanges as sender 
    user_id = Column(types.Integer, ForeignKey('user.id'))
    user = relationship('User', backref="messages",
                    foreign_keys="Message.user_id")
   

    def __repr__(self) -> str:
        return f"<Message (id={self.id} readable={self.is_readable})>"