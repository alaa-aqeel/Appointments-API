from core.database.model import Model, Column, types, relationship, ForeignKey
from app.schemas.work_hours import WorkHoursReadOnly

class WorkHours(Model):

    __schema__ = WorkHoursReadOnly

  
    date = Column(types.Date)
    from_hour = Column(types.Time)
    to_hour = Column(types.Time)
    desc = Column(types.Text, nullable=True)
    is_active = Column(types.Boolean, default=True)
    
    # One Employee TO Many WorkHours
    employee_id = Column(types.Integer, ForeignKey('employee.id'))
    employee = relationship("Employee", 
                    backref="work_hours", 
                    foreign_keys="WorkHours.employee_id")

    def __repr__(self) -> str:
        return f"<WorkHours (date={self.date}, hours=({self.from_hour}, {self.to_hour}))>"