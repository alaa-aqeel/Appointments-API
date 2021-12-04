from datetime import date, timedelta
from database.model import Model, Column, types, relationship, TimeStamp
from app.schemas import CustomerReadOnly

class Customer(Model, TimeStamp):

    __schema__ = CustomerReadOnly

    fullname = Column(types.String(45))
    phone = Column(types.String(15))
    email = Column(types.String(45), nullable=True)
    birthdate = Column(types.Date())
    gender = Column(types.Enum('female', 'male', name="gender_enum", create_type=False))

    @property
    def age(self):
        return (date.today() - self.birthdate) // timedelta(days=365)

    def __repr__(self) -> str:

        return f"<Customer (fullname={self.fullname}, id={self.id})>"