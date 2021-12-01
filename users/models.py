from database.model import Model, TimeStamp, Column, types


class User(Model, TimeStamp):

    username = Column(types.String(45), unique=True)
    password = Column(types.String)
    last_login = Column(types.DateTime)
    is_active = Column(types.Boolean, default=0)
    is_super  = Column(types.Boolean, default=0)


    def __repr__(self) -> str:
        return f"<User (username={self.username})>"