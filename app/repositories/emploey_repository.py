from fastapi.exceptions import HTTPException
from app.models import WorkHours, Employee
from app.repositories import BaseRepository 


class EmployeeRepository(BaseRepository):

    def __init__(self):
        self.model = Employee

    def get(self, id) -> Employee:
        """Get employee by id"""
        
        return self.get_or_failed(Employee, id)

    def get_work_hours(self, employee_id, is_actived=True):
        """Get work hours for employee"""
        return WorkHours.query.filter(
            WorkHours.employee_id==employee_id,
            WorkHours.is_active==is_actived).all()

    def all(self, *args, **kw) -> list:
        
        return self.__filter_employee(*args, **kw)

    def __filter_by_category(self, category: int) -> Employee:
        """Fiter employee by category"""

        return self.model.query.filter(self.model.category_id==category)

    def __filter_employee(self, 
            category: int=0, 
            name: str= "", 
            special: str="") -> Employee:
        """Filter employee by kw"""

        objs = self.model.query.filter(
                self.model.fullname.like(f"%{name}%"),
                self.model.special.like(f"%{special}%"))
        
        if category:
            objs = self.__filter_by_category(category)

        return objs
    