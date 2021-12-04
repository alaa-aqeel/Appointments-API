from datetime import date, timedelta
from database.model import Model, Column, types, relationship, TimeStamp, ForeignKey, backref
from app.schemas import CustomerReadOnly

class Customer(Model, TimeStamp):

    __schema__ = CustomerReadOnly

    fullname = Column(types.String(45))
    phone = Column(types.String(15))
    email = Column(types.String(45), nullable=True)
    birthdate = Column(types.Date())
    gender = Column(types.Enum('female', 'male', name="gender_enum", create_type=False))

    # One TO One with User Model
    user_id = Column(types.Integer, ForeignKey('user.id'))
    account = relationship("User", 
                    backref=backref("customer", uselist=False), 
                    foreign_keys="Customer.user_id")

    @property
    def age(self) -> int:
        return (date.today() - self.birthdate) // timedelta(days=365)

    def set_account(self, user: object) -> None:
        self.user = user
        self.save()



    def __repr__(self) -> str:

        return f"<Customer (fullname={self.fullname}, id={self.id})>"