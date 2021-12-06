from fastapi.exceptions import HTTPException
from app.models import Role, User, Customer, Employee
from app.repositories import BaseRepository 




class UserRepository(BaseRepository):

    def __init__(self):
        self.model = User 

    def __create_customer_profile(self, user: User, **kw):
        """Create profile customer"""
        _customer = Customer.create(**kw)
        user.customer = _customer
        user.save()
        
        return self.customer 

    def __create_employee_profile(self, user: User, **kw):
        """Create profile employee"""
        _employee = Employee.create(**kw)
        user.employee = _employee
        user.save()

        return self.employee 
             
    def create_profile(self, user: User,**kw:dict):
        """Create profile customer or employee"""

        # Employee, Customer
        if not self.customer and self.has_roles(["customer"]):
            return self.__create_customer_profile(user, **kw)

        if not self.employee and self.has_roles(["employee"]):
            return self.__create_employee_profile(user, **kw)

        raise HTTPException(404, detail={
            "ok": False,
            "msg": "Not found profile"
        })

    def set_role(self, user, roleId: int) -> None:
        """set role for user by role Id"""

        if roleId:
            user.role = self.get_role(roleId)
            user.save()

    def get_role(self, roleId):
        """set role by role Id"""

        role = Role.get(roleId) 
        if role:
            return role 

        raise HTTPException(status_code=404, detail={
            'ok': False,
            'msg': f"NOT found role {id}",
            "data": {
                "id": id
            }
        })

    def create(self, **kw):
        """create new user"""

        role = kw.pop('role', 1)
        user = super().create(**kw)
        self.set_role(user, role)

        return user

    def update(self, id, **kw):
        """create new user"""

        role = kw.pop('role', 1)
        user = super().update(id, **kw)
        self.set_role(user, role)

        return user 
