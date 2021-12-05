from core.database.model import Model, Column, types, relationship, ForeignKey, TimeStamp


class Appointment(Model, TimeStamp):


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

    def __repr__(self) -> str:
        return f"<Appointment (status={self.status}, id={self.id})>"