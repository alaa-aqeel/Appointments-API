from typing import Set
from pydantic import BaseSettings


class Setting(BaseSettings):

    APP_NAME: str = "Appointment-API"
    DATABASE_URL: str = "sqlite:///./sqlite.db"
    # "postgresql://user:password@postgresserver/db"
    class Config: 

        env_file: str = ".env"

setting = Setting() 