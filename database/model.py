from sqlalchemy import exc
from database import Base, SessionLocal

# Base
class Model():

    session = SessionLocal()
    
    @classmethod 
    def create(cls, **kw):
        """Create new object"""
        try: 
            obj = cls(**kw)
            cls.session(obj)
            cls.session.commit()
            return True, obj 
        except exc.SQLAlchemyError as err:
            return False, str(err.__dict__.get("orig", ""))