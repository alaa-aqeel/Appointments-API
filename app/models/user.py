from fastapi.exceptions import HTTPException
from sqlalchemy.sql.expression import false
from database.model import Model, TimeStamp, Column, ForeignKey, types, relationship
from app.func import generate_password_hash, verify_password
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


    def has_roles(self, names: list):
        return self.role.name in names

    @property
    def get_profile(self):

        if self.customer and self.has_role(["customer"]):
            return self.customer 

        if self.employee and self.has_role(["employee"]):
            return self.employee 

        raise HTTPException(404, detail={
            "ok": False,
            "msg": "Not found profile"
        })
        
    def create_profile(self, **kw:dict):
        """Create profile customer or employee"""

        # Employee, Customer
        if self.customer and self.has_role(["customer"]):
            _customer = customer.Customer(**kw)
            self.customer = _customer
            self.save()
            
            return self.customer 

        if self.employee and self.has_role(["employee"]):
            _employee = employee.Employee(**kw)
            self.employee = _employee
            self.save()

            return self.employee 

        raise HTTPException(404, detail={
            "ok": False,
            "msg": "Not found profile"
        })


    @classmethod
    def create(cls, **kw):
        kw["password"] = generate_password_hash(kw['password'])
        
        return super().create(**kw)

    def update(self, **kw):
        if kw.get("password"):
            kw["password"] = generate_password_hash(kw['password'])
        return super().update(**kw)

    @classmethod
    def login(cls, username: str, password: str):
        user = cls.query.filter_by(username=username).first()
        
        if user:
            if verify_password(password, user.password):
                return user


    def set_role(self, roleId: int) -> None:
        self.role = role.Role.get(roleId)
        self.save()

    def __repr__(self) -> str:
        return f"<User (username={self.username}, id={self.id})>"