from fastapi.exceptions import HTTPException
from app.models import WorkHours
from app.repositories import BaseRepository 



class WorkHoursRepository(BaseRepository):

    def __init__(self, employee):
        self.model = WorkHours
        self.employee = employee
        

    @property
    def filter_employee(self):
        """Filter work hours by employee """
        return self.model.query.filter(self.model.employee==self.employee)

    def all(self): 
        """Get work hours for employee"""
        
        return self.filter_employee.all()

    def get(self,id: int): 
        """Get work hour for employee by id"""
  
        return self.get_or_failed(self.model, id, self.filter_employee)


    def update(self, id, **kw):
        """update  work hours by id"""
        obj = self.get(id)
        obj.save(**kw)
        return obj

    def create(self, **kw):
        """create new work """
        kw['employee'] = self.employee 
        new_obj = self.model.create(**kw)
        return new_obj


    def delete(self, id):
        """Delete work hours by id"""
        obj = self.get(id)
        obj.delete()
        return obj