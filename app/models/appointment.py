from core.database.model import (Model, 
                        Column, types,  relationship, 
                        ForeignKey, TimeStamp)
                        
from app.schemas.appointment import AppointmentReadOnly

class Appointment(Model, TimeStamp):

    __schema__ = AppointmentReadOnly

    desc = Column(types.Text, nullable=True)
    status = Column(types.Enum('await', "confirm", "unconfirm", "cancel"), default="await")

    # One Customer TO Many Appointment
    customer_id = Column(types.Integer, ForeignKey('customer.id'))
    customer = relationship("Customer", 
                    backref="appointments", 
                    foreign_keys="Appointment.customer_id")

    # One Employee TO Many Appointment
    employee_id = Column(types.Integer, ForeignKey('employee.id'))
    employee = relationship("Employee", 
                    backref="appointments", 
                    foreign_keys="Appointment.employee_id")

    # One WorkHours TO Many Appointment
    date_id = Column(types.Integer, ForeignKey('workhours.id'))
    date = relationship("WorkHours", 
                    backref="appointments", 
                    foreign_keys="Appointment.date_id")


    @classmethod
    def filter_date(cls, date):
        return cls.query.filter(Appointment.date.has(date=date))

    def __repr__(self) -> str:
        return f"<Appointment (status={self.status}, id={self.id})>"