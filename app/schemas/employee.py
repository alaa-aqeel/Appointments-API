from datetime import date, time
from enum import Enum
from core.database.schema import BaseModel
from app.schemas.profile import CustomerReadOnly, EmployeeReadOnly, Optional

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
    

class Appointment(BaseModel):
    desc: Optional[str]
    date: int
    

    class Config:
        orm_mode = True


class StatusEum(str, Enum):
    _await = 'await'
    confirm = "confirm"
    uncofirm = "unconfirm"
    cancel = "cancel"

# for employee
class AppointmentEmployee(BaseModel):
    date: int
    status: StatusEum = StatusEum._await

    class Config:
        orm_mode = True
        
class AppointmentReadOnly(Appointment):
    id: int 
    status: StatusEum = StatusEum._await
    
    date: WorkHoursReadOnly
    

class AppointmentEmployeeReadOnly(AppointmentReadOnly):
     employee: EmployeeReadOnly

class AppointmentCustomerReadOnly(AppointmentReadOnly):
    customer: CustomerReadOnly
     