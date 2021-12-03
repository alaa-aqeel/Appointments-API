from typing import Set
from pydantic import BaseSettings


class Setting(BaseSettings):

    APP_NAME: str = "Appointment-API"
    DATABASE: dict = {
        "url": "sqlite:///./sqlite.db",
        "connect_args":{
            "check_same_thread": False
        }

    }
    # "postgresql://user:password@postgresserver/db"
    class Config: 

        env_file: str = ".env"

setting = Setting() 