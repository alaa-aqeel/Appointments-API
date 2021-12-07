from fastapi import APIRouter, Request
from core.depends import AuthorizeRole, Profile
from core.resource import resource , BaseResource
from app.repositories.work_hours_repository import WorkHoursRepository
from app.repositories.appointment_repository import AppointmentRepository
from app.schemas.appointment import AppointmentEmployee
from app.schemas.work_hours import WorkHours as WorkHoursSchema
from app.models.appointment import Appointment as AppointmentModel

router = APIRouter(
    prefix="/employee",
    dependencies=[AuthorizeRole(["employee"])]
)

@resource(router, path="/workhorus")
class WorkHoursResource(BaseResource):

    
    def __init__(self, request: Request, employee=Profile):
        
        super().__init__(request)
        # Set employee to BaseRepostory
        self.repository = WorkHoursRepository(employee)

    def index(self):
        """Get All WorkHours"""

        return self.repository.all()

    def update(self, id, schema: WorkHoursSchema):
        """Update  WorkHour"""

        obj = self.repository.update(id, **schema.dict(exclude_unset=True))
        return self.response(
            msg="Successfuly update", 
            data=obj.parse())

    def store(self, schema: WorkHoursSchema):
        """Create  new WorkHour"""

        obj = self.repository.create(**schema.dict())
        return self.response(
            msg="Successfuly create", 
            data=obj.parse())

    def delete(self, id):
        """Delete WorkHour"""

        is_ok = self.repository.delete(id)
        return self.response(ok=bool(is_ok), data={"id": id})


@resource(router, path="/appointment")
class AppointmentResource(BaseResource):
    
    def __init__(self, request: Request, employee=Profile):
        
        super().__init__(request)
        # Set employee to BaseRepostory
        self.repository = AppointmentRepository(employee)

    def index(self):    
        """Get All WorkHour"""

        data = self.repository.all()
 
        return AppointmentModel.parse_all(data)

    def update(self, id, schema: AppointmentEmployee):
        """Update  Appointment"""

        obj = self.repository.update(id, **schema.dict(exclude_unset=True))
        return self.response(
            msg="Successfuly update", 
            data=obj.parse())