from sqlalchemy import exc
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.sql import sqltypes as types
from sqlalchemy import Column
from database import SessionLocal, engine


class CustomProperty(property):
    
    def __get__(self, _, cls):
        return self.fget(cls)

# Base Model
class BaseModel(object):
    
    session = SessionLocal()

    id = Column(types.Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @CustomProperty  
    def query(cls):
        return cls.session.query(cls)



    @classmethod 
    def create(cls, **kw):
        """Create new object"""
        try: 
            obj = cls(**kw)
            cls.session.add(obj)
            cls.session.commit()
            return True, obj 
        except exc.SQLAlchemyError as err:
            return False, str(err.__dict__.get("orig", ""))

    def save(self):
        self.session.add(self)
        self.session.commit()
        
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id}/>"
    

Model = declarative_base(cls=BaseModel)

def migrate():
    Model.metadata.create_all(bind=engine)
