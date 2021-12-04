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

    # One Employee TO One with User account
    account_id = Column(types.Integer, ForeignKey('user.id'))
    account = relationship("User", 
                    backref=backref("employee", uselist=False), 
                    foreign_keys="Employee.account_id")

    # Many Employees To One Category
    category_id = Column(types.Integer, ForeignKey('category.id'))
    category = relationship("Category", 
                    backref=backref("employees", uselist=False), 
                    foreign_keys="Employee.category_id")

    # Many Employees To One User Manager
    manager_id = Column(types.Integer, ForeignKey('user.id'))
    manager = relationship("User", 
                    backref=backref("employees", uselist=False), 
                    foreign_keys="Employee.manager_id")


    # Set category by CategoryModel
    def set_category(self, category):
        self.category = category
        self.save()

    # Set user 
    def set_account(self, user: object) -> None:
        self.user = user
        self.save()

    def __repr__(self) -> str:
        return f"<Employee (fullname={self.fullname}, id={self.id})>"