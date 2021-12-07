import os 
from typing import Set
from pydantic import BaseSettings


class Setting(BaseSettings):

    authjwt_secret_key: str = "SECRETKEY"
    authjwt_denylist_enabled: bool = True
    app_name: str = "Appointment-API"
    database: dict = {
        "url": "sqlite:///./sqlite.db",
        "connect_args":{
            "check_same_thread": False
        }

    }
    # "postgresql://user:password@postgresserver/db"

    allow_origins = [
        "http://127.0.0.1:8000",
        "http://localhost:8080",
    ]

    storage_path = "storage"

    class Config: 

        env_file: str = ".env"

setting = Setting() 