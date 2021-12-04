from database.model import Model, Column, types, relationship
from app.schemas.user import Role

class Role(Model):

    __schema__ = Role

    name = Column(types.String(45), unique=True)
    desc = Column(types.TEXT) 
    users = relationship('User', back_populates="role")

    def __repr__(self) -> str:
        return f"<Role (name={self.name}, id={self.id})>"