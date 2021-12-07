from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from core.setting import setting

engine = create_engine(
    url=setting.database_url[setting.env],
    **setting.engine_args)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def get_session():
    db = SessionLocal()
    try: 
        yield db 
    finally:
        db.close()