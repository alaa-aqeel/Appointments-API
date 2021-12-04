from datetime import date, timedelta
from database.model import Model, Column, types, relationship, TimeStamp, ForeignKey, backref
from app.schemas import CustomerReadOnly

class Category(Model, TimeStamp):

    name = Column(types.String(45), unique=True)
    avatar = Column(types.String(255), nullable=True)
    
    def __repr__(self) -> str:
        return f"<Category (name={self.name}, id={self.id})>"