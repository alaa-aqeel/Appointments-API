from sqlalchemy import or_
from fastapi.exceptions import HTTPException
from app.models import Appointment, WorkHours, Employee, Customer
from app.schemas.employee import StatusEum
from app.repositories import BaseRepository 


class AppointmentRepository(BaseRepository):

    def __init__(self, _for):
        self.model = Appointment
        self._for  = _for

    def all(self, date=''):
        """Get all for customer or employee"""
        if date:
            return self.__query_for().filter(
                    Appointment.date.has(date=date)
                ).all()
        
        return self.__query_for().all()

    def __query_for(self) -> Appointment:
        """Query for it"""
        return Appointment.query.filter(
                or_(Appointment.customer==self._for),
                or_(Appointment.employee==self._for)
            )


    def get(self, id: int) -> Appointment:
        """Get Appointment by id"""
        return self.get_or_failed(Appointment, id, self.__query_for())

    def get_work_hours(self, id):
        __filter = WorkHours.query.filter(WorkHours.is_active==True)
        return self.get_or_failed(WorkHours, id, __filter)

    def create(self, customer: Customer, dateId: int, desc: str="") -> Appointment:
        """Book appointment for customer"""

        date = self.get_work_hours(dateId)
        obj = super().create(
                employee=date.employee,
                customer=customer,
                desc=desc,
                date=date)

        return obj


    def update(self, id, date: int, status: str= StatusEum.confirm):

        date = self.get_work_hours(date)
        obj = self.model.update(id, **{
            'employee_id': date.employee_id,
            "date_id": date.id, 
            "status": status.value
        })
    
        return obj