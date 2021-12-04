from database.model import Model, Column, types

class Category(Model):

    name = Column(types.String(45), unique=True)
    avatar = Column(types.String(255), nullable=True)
    
    def __repr__(self) -> str:
        return f"<Category (name={self.name}, id={self.id})>"