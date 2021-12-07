from fastapi import Body, APIRouter
from core.resource import resource, BaseResource
from app.models import Appointment
from app.schemas.appointment import AppointmentAdminReadOnly


router = APIRouter(prefix="/appointment")

@resource(router)
class UserResource(BaseResource):



    def index(self, date: str=None, employee: int= None, customer: int= None):
        
        model = Appointment.query
        if date:
            model = Appointment.filter_date(date)
        
        if employee:
           model = model.filter(Appointment.employee_id==employee)
        
        if customer:
            model = model.filter(Appointment.customer_id==customer)

        return  Appointment.parse_all(model=model.all() if model else None)

    def show(self, id):
        obj = Appointment.get(id) 
        if obj:
            return obj.parse(AppointmentAdminReadOnly)

        self.abort(404, {"msg": f"Not found appointment {id}"})
