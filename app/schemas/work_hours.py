from datetime import date, time
from core.database.schema import BaseModel

class WorkHours(BaseModel):
    date: date
    from_hour: time
    to_hour: time
    desc: str
    is_active: bool
    
    class Config:
        orm_mode=True

class WorkHoursReadOnly(WorkHours):
    id: int 