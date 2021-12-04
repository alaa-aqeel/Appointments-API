from fastapi.exceptions import HTTPException
from sqlalchemy.sql.expression import false
from app.models.customer import Customer
from database.model import Model, TimeStamp, Column, ForeignKey, types, relationship
from app.func import generate_password_hash, verify_password
from app.models import Role
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


    def has_roles(self, names: list):
        return self.role.name in names

    @property
    def get_profile_customer(self):

        if self.customer and self.has_role(["customer"]):
            return self.customer 

        raise HTTPException(404, detail={
            "ok": False,
            "msg": "Not found profile customer"
        })
        

    @classmethod
    def create(cls, **kw):
        kw["password"] = generate_password_hash(kw['password'])
        
        return super().create(**kw)

    @classmethod
    def login(cls, username: str, password: str):
        user = cls.query.filter_by(username=username).first()
        
        if user:
            if verify_password(password, user.password):
                return user


    def set_role(self, roleId: int) -> None:
        self.role = Role.get(roleId)
        self.save()

    def __repr__(self) -> str:
        return f"<User (username={self.username}, id={self.id})>"