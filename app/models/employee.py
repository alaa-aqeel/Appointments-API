from datetime import date, timedelta
from database.model import Model, Column, types, relationship, TimeStamp, ForeignKey, backref
from app.schemas import CustomerReadOnly

class Employee(Model, TimeStamp):

    __schema__ = CustomerReadOnly

    fullname = Column(types.String(45))
    phone = Column(types.String(15))
    email = Column(types.String(45), nullable=True)
    avatar = Column(types.String(255), nullable=True)
    about = Column(types.Text, nullable=True)
    special = Column(types.String(45))
    address = Column(types.String(255), nullable=True)
    price = Column(types.Integer, nullable=True)
    gender = Column(types.Enum('female', 'male', name="gender_enum", create_type=False))

    # One TO One with User Model
    user_id = Column(types.Integer, ForeignKey('user.id'))
    account = relationship("User", 
                    backref="employees", 
                    foreign_keys="Employee.user_id")



    def set_account(self, user: object) -> None:
        self.user = user
        self.save()

    def __repr__(self) -> str:

        return f"<Employee (fullname={self.fullname}, id={self.id})>"