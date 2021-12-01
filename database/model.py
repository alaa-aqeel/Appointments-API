from sqlalchemy import exc, Column, func, ForeignKey
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.sql import sqltypes as types
from database import SessionLocal, engine

class CustomProperty(property):
    """Custom Property To call func"""

    def __get__(self, _, cls):
        return self.fget(cls)

# Base Model
class BaseModel(object):
    """Base Model for  SqlAlchemy Model"""

    session:object = SessionLocal()

    id:Column = Column(types.Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(cls) -> str:
        """Set a class name for the table """
        return cls.__name__.lower()

    @CustomProperty  
    def query(cls) -> object:
        """Get session query """
        return cls.session.query(cls)

    @classmethod 
    def create(cls, **kw:dict) -> list:
        """Create new raw"""
        try: 
            obj = cls(**kw)
            cls.session.add(obj)
            cls.session.commit()
            return True, obj 
        except exc.SQLAlchemyError as err:
            return False, str(err.__dict__.get("orig", ""))

    def save(self) -> list:
        """Commit object"""
        try: 
            self.session.add(self)
            self.session.commit()
            self.session.refresh(self)
            return True, self
        except exc.SQLAlchemyError as err:
            return False, str(err.__dict__.get("orig", ""))
        
    def __repr__(self) -> str:

        return f"<{self.__class__.__name__}(id={self.id})>"
    

class TimeStamp(object):
    """Timestamp fields"""
    
    created_at = Column(types.TIMESTAMP, server_default=func.now())
    updated_at = Column(types.TIMESTAMP, server_default=func.now() , server_onupdate=func.now())

Model = declarative_base(cls=BaseModel)

def migrate():
    
    Model.metadata.create_all(bind=engine)
