from fastapi.exceptions import HTTPException
from sqlalchemy.sql.expression import false
from core.database.model import Model, TimeStamp, Column, ForeignKey, types, relationship
from core.func import generate_password_hash, verify_password
from app.models import role, customer, employee
from app.schemas import user

class User(Model, TimeStamp):

    __schema__ = user.UserReadOnly

    username = Column(types.String(45), unique=True)
    password = Column(types.String)
    last_login = Column(types.DateTime, nullable=True)
    is_active = Column(types.Boolean, default=0)
    is_super  = Column(types.Boolean, default=0)

    role_id = Column(types.Integer, ForeignKey('role.id'))
    role = relationship('Role', back_populates="users")

    chats = relationship("Chat",
        secondary="chats_users",
        back_populates="users")

    def has_roles(self, names: list):
        return self.role.name in names

    @property
    def profile(self):

        if self.customer and self.has_roles(["customer"]):
            return self.customer 

        if self.employee and self.has_roles(["employee"]):
            return self.employee 

    @classmethod
    def create(cls, **kw):
        kw["password"] = generate_password_hash(kw['password'])
        return super().create(**kw)

    def update(self, **kw):
        if password := kw.get("password", None):
            kw['password'] = generate_password_hash(password)
        return super().save(**kw)

    @classmethod
    def login(cls, username: str, password: str):

        user = cls.query.filter_by(username=username).first()
        return  user if user and verify_password(password, user.password) else None 

    def __repr__(self) -> str:
        return f"<User (username={self.username}, id={self.id})>"