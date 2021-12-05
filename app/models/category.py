from core.database.model import Model, Column, types
from app.schemas.category import CategoryReadOnly



class Category(Model):

    __schema__ = CategoryReadOnly

    name = Column(types.String(45), unique=True)
    avatar = Column(types.String(255), nullable=True)
    
    def __repr__(self) -> str:
        return f"<Category (name={self.name}, id={self.id})>"