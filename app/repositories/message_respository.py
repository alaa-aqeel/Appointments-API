
from fastapi.exceptions import HTTPException
from sqlalchemy.sql.expression import or_
from app.models import Message, Chat, User
from app.repositories import BaseRepository 


class MessengerRepository(BaseRepository):

    def __init__(self, user):
        self.model = Message
        self.current_user = user


    def chat_current_user(self):
        """Get all chat for current user"""

        return Chat.query.join(Chat.users).filter(User.id==self.current_user.id)

    def chat_user_query(self, user): # { 
        
        return Chat.session.query(Chat.id).join(Chat.users).filter(User.id==user.id)
    #}

    
    def chat_between_users(self, user1, user2):# { 

        chats = Chat.query.join(Chat.users).filter(
            or_(User.id==user1.id, User.id==user2.id),
            Chat.id.in_(self.chat_user_query(user1)),
            Chat.id.in_(self.chat_user_query(user2)),
        )

        return chats
    #}

    def chat_with(self, user):# { 
        
        return self.chat_between_users(self.current_user, user)
    #}

    def create_message(self, text, chat):# {

        return Message.create(text=text, user=self.current_user, chat=chat)
    # } 

    def create_chat(self, user_1, user_2):# {

        chat = Chat.create()
        chat.users = [user_1, user_2]
        chat.save()
        return chat
    #}

    def create(self, text, to): # {

        to_user = self.get_or_failed(User, to) 
        chat = self.chat_with(to_user).first()
        if not chat:
            chat = self.create_chat(to_user, self.current_user)

        msg = self.create_message(text, chat)
        
        return msg
    # }

    def get_message(self, msgId): #{ 

        return self.get_or_failed(Message, msgId, Message.query.filter(
                        Message.user.has(id=self.current_user.id)
                    ))
    #}
        

    def update(self, msgId, text): #{ 

        msg = self.get_message(msgId)
        print(msg)
        msg.text = text 
        msg.save()
        return msg
    #}

    def delete(self, msgId): # {
        msg = self.get_message(msgId)   
        msg.delete()
        return msg 
    #}