from sqlalchemy.orm import validates
from database.model import Model, Column, types, relationship
from database.validations import import_class
from app.schemas import user

class Role(Model):

    __schema__ = user.RoleReadOnly

    name = Column(types.String(45), unique=True)
    desc = Column(types.TEXT) 
    users = relationship('User', back_populates="role")

    def __repr__(self) -> str:
        return f"<Role (name={self.name}, id={self.id})>"