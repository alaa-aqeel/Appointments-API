from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.orm import sessionmaker, scoped_session
from core.setting import setting

engine = create_engine(**setting.database)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def get_session():
    db = SessionLocal()
    try: 
        yield db 
    finally:
        db.close()