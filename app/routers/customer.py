from fastapi import APIRouter, Request, HTTPException
from core.resource import resource , BaseResource
from core.depends import AuthorizeRole, Profile
from app.models import Employee, WorkHours, Appointment
from app.schemas.appointment import Appointment as  AppointmentSchema, Appointment as  AppointmentSchema
from app.repositories.emploey_repository import EmployeeRepository 
from app.repositories.appointment_repository import AppointmentRepository 


router = APIRouter(
    prefix="/customer",
    dependencies=[AuthorizeRole(["customer"])])

@resource(router, path="/employee")
class EmployeeResource(BaseResource):

    repository = EmployeeRepository()

    def index(self, 
            category: int=0, 
            name: str= "", 
            special: str=""):
        """Get employee by category"""

        _filter = self.repository.all(category, name, special)
        return Employee.parse_all(_filter.all())

    def show(self, id):

        """Get Workhours form employes by id"""
        objs = self.repository.get_work_hours(id)
        return WorkHours.parse_all(objs)


@resource(router, path="/appointment")
class AppointmentResource(BaseResource):


    def __init__(self, request: Request, profile= Profile):
        super().__init__(request)
        
        self.customer = profile
        self.repository = AppointmentRepository(self.customer)


    def index(self, date: str=""):

        return Appointment.parse_all(self.repository.all(date)) 

    def store(self, scheam: AppointmentSchema):
        
        new_obj = self.repository.create(
                    self.customer, 
                    scheam.date, 
                    scheam.desc)

        return self.response(msg="Successfuly book appointment success", data=new_obj.parse())

    def delete(self, id):

        obj = self.repository.get_or_failed(Appointment, id)
        obj.status = "cancel"
        obj.save()

        return self.response(msg="cancel success", data=obj.parse())