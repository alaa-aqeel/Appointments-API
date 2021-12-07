from enum import Enum
from core.database.schema import BaseModel
from app.schemas.profile import CustomerReadOnly, EmployeeReadOnly, Optional
from app.schemas.work_hours import WorkHoursReadOnly


    
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
    status:  Optional[StatusEum] = StatusEum._await
    date: Optional[WorkHoursReadOnly]
    

class AppointmentEmployeeReadOnly(AppointmentReadOnly):
    employee: EmployeeReadOnly


class AppointmentCustomerReadOnly(AppointmentReadOnly):
    customer: CustomerReadOnly

class AppointmentAdminReadOnly(AppointmentReadOnly):
    customer: CustomerReadOnly
    employee: EmployeeReadOnly