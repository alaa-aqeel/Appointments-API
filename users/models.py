from database.model import Model, TimeStamp, Column, ForeignKey, types, relationship
# from users import schemas

class Role(Model):

    # __schema__ = schemas.Role

    name = Column(types.String(45), unique=True)
    desc = Column(types.TEXT) 
    users = relationship("User", back_populates="role")

    def __repr__(self) -> str:
        return f"<Role (name={self.name}, id={self.id})>"


class User(Model, TimeStamp):

    # __schema__ = schemas.UserReadOnly

    username = Column(types.String(45), unique=True)
    password = Column(types.String)
    last_login = Column(types.DateTime, nullable=True)
    is_active = Column(types.Boolean, default=0)
    is_super  = Column(types.Boolean, default=0)

    role_id = Column(types.Integer, ForeignKey('role.id'))
    role = relationship(Role, back_populates="users")

    def set_role(self, roleId: int) -> None:
        self.role = Role.get(roleId)
        self.save()

    def __repr__(self) -> str:
        return f"<User (username={self.username}, id={self.id})>"