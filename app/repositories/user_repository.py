from fastapi.exceptions import HTTPException
from app.models import Role, User, Customer, Employee, Category
from app.repositories import BaseRepository 




class UserRepository(BaseRepository):

    def __init__(self):
        self.model = User 

    
    def all(self, role=None):

        if role := Role.get(role):
            objs = User.query.filter(User.role==role).all()
            return User.parse_all(model=objs)

        return User.parse_all()

    def get_category(self, categoryId):
        category = Category.get(categoryId) 
        if category:
            return category 

        raise HTTPException(status_code=404, detail={
            'ok': False,
            'msg': f"Not found category {categoryId}",
            "data": {
                "id": categoryId
            }
        })

    def __create_customer_profile(self, user: User, **kw):
        """Create profile customer"""
        _customer = Customer.create(**kw)
        user.customer = _customer
        user.save()
        
        return _customer

    def __create_employee_profile(self, user: User, **kw):
        """Create profile employee"""

        kw["category"] = self.get_category(kw.pop('category'))
        _employee = Employee.create(**kw)
        user.employee = _employee
        user.save()

        return _employee
             
    def create_profile(self, user: User,**kw:dict):
        """Create profile customer or employee"""

        # Employee, Customer
        if not user.customer and user.has_roles(["customer"]):
            return self.__create_customer_profile(user, **kw)

        if not user.employee and user.has_roles(["employee"]):
            return self.__create_employee_profile(user, **kw)

        raise HTTPException(404, detail={
            "ok": False,
            "msg": "Not found profile"
        })

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

        kw['role'] = self.get_role(kw.get('role', 1))
        user = super().create(**kw)

        return user

    def update(self, id, **kw):
        """create new user"""
        
        if roleId := kw.pop("role", None):
            kw['role_id'] = self.get_role(roleId).id
        user = super().update(id, **kw)
        return user 
